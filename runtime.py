"""smolagents runtime: ToolCallingAgents driven by an offline Model.

Each agent is a smolagents ToolCallingAgent with a `lookup_role` tool. The
offline model first calls that tool, then ends with `final_answer`, so the
real ReAct loop (model -> tool call -> observation -> final answer) is exercised.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from smolagents import Tool, ToolCallingAgent
from smolagents.models import (ChatMessage, ChatMessageToolCall,
                               ChatMessageToolCallFunction, Model)

from common.flow import compose_input, dependencies, execution_layers, system_prompt
from common.offline_llm import offline_complete


class LookupRole(Tool):
    name = "lookup_role"
    description = "Returns the responsibilities of this agent's role."
    inputs: dict = {}
    output_type = "string"

    def __init__(self, role: str, instruction: str):
        super().__init__()
        self._text = f"{role}: {instruction}"

    def forward(self) -> str:
        return self._text


class OfflineModel(Model):
    """Scripted model: step 1 calls lookup_role, step 2 calls final_answer."""

    def __init__(self, role: str, instruction: str):
        super().__init__(model_id="offline")
        self.role, self.instruction = role, instruction
        self.prompt = ""
        self.step = 0

    def _call(self, name: str, arguments: dict) -> ChatMessage:
        return ChatMessage(role="assistant", content=None, tool_calls=[ChatMessageToolCall(
            id=f"call_{self.step}", type="function",
            function=ChatMessageToolCallFunction(name=name, arguments=arguments))])

    def generate(self, messages, stop_sequences=None, response_format=None,
                 tools_to_call_from=None, **kwargs) -> ChatMessage:
        self.step += 1
        if self.step == 1:
            return self._call("lookup_role", {})
        text = offline_complete(system_prompt(self.role, self.instruction), self.prompt)
        return self._call("final_answer", {"answer": text})


def make_agent(role: str, instruction: str, model=None) -> tuple[ToolCallingAgent, Model]:
    model = model or OfflineModel(role, instruction)
    agent = ToolCallingAgent(tools=[LookupRole(role, instruction)], model=model, max_steps=4,
                             name=role.lower().replace(" ", "_").replace("-", "_"),
                             description=instruction, verbosity_level=0)
    return agent, model


def run_app(title, agents, task, pattern="sequential", provider=None) -> dict:
    deps = dependencies(pattern, len(agents))
    outputs: dict[str, str] = {}

    def call(i: int):
        key, role, instr = agents[i]
        agent, model = make_agent(role, instr)  # fresh agent per run: clean memory
        ups = [(agents[j][1], outputs[agents[j][0]]) for j in deps[i]]
        prompt = compose_input(task, ups)
        model.prompt = prompt
        return key, str(agent.run(prompt))

    for layer in execution_layers(pattern, len(agents)):
        if len(layer) == 1:
            k, v = call(layer[0])
            outputs[k] = v
        else:
            with ThreadPoolExecutor(max_workers=len(layer)) as pool:
                for k, v in pool.map(call, layer):
                    outputs[k] = v
    return {key: outputs[key] for key, _, _ in agents}
