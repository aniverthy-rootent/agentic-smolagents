"""Framework-neutral description of how agents hand data to each other.

Patterns
--------
sequential : agent i receives the task plus the output of agent i-1.
fanout     : agent 0 plans; the middle agents all work in parallel on the plan;
             the last agent merges every middle output.
Each framework runtime maps these dependencies onto its own primitives
(graph edges, task context, group chat order, workflow steps, ...).
"""
from __future__ import annotations

SEQUENTIAL = "sequential"
FANOUT = "fanout"


def dependencies(pattern: str, n: int) -> list[list[int]]:
    """For each agent index, the indexes whose outputs it consumes."""
    if pattern == FANOUT and n >= 4:
        deps: list[list[int]] = [[]]
        deps += [[0] for _ in range(1, n - 1)]
        deps.append(list(range(1, n - 1)))
        return deps
    return [[]] + [[i - 1] for i in range(1, n)]


def execution_layers(pattern: str, n: int) -> list[list[int]]:
    """Groups of agents that may run concurrently, in order."""
    if pattern == FANOUT and n >= 4:
        return [[0], list(range(1, n - 1)), [n - 1]]
    return [[i] for i in range(n)]


def compose_input(task: str, dep_outputs: list[tuple[str, str]]) -> str:
    """Build the user message for an agent from the task and upstream outputs."""
    if not dep_outputs:
        return f"Task: {task}"
    upstream = "\n".join(f"- {name}: {text}" for name, text in dep_outputs)
    return f"Task: {task}\n\nUpstream results:\n{upstream}"


def system_prompt(role: str, instruction: str) -> str:
    return f"{role}\nYou are the {role} in a multi-agent team. {instruction}"
