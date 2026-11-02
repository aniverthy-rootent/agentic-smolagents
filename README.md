# agentic-smolagents

**11 multi-agent applications built with smolagents (Hugging Face).**  
Theme: _Science, research & code-writing agents_

[smolagents](https://github.com/huggingface/smolagents) is Hugging Face's minimal agent library (tool-calling and code-writing agents). These apps focus on science, research and code-writing workflows.

## Quick start (no API key needed)

```bash
pip install -r requirements.txt
python run_all.py                       # run all 11 apps
python -m apps.app01_paper_replication   # run a single app
pytest -q                               # smoke tests for every app
```

Every app runs against a deterministic offline model (`common/offline_llm.py`) so you can watch the orchestration work without credentials.

## How it works

Each agent is a real `ToolCallingAgent` with a tool. An offline scripted `Model` makes the genuine ReAct loop run: tool call, observation, then `final_answer`. Parallel layers run in a thread pool.

## Using a real model

Replace `OfflineModel` with `InferenceClientModel()`, `LiteLLMModel('anthropic/claude-sonnet-5-5')`, `OpenAIServerModel(...)` or `TransformersModel(...)` and swap in `CodeAgent` if you want agents that write Python.

## Applications

| # | Application | Agents | Roles |
|---|---|---|---|
| 1 | Paper Replication | 5 | Paper Reader, Environment Planner, Code Drafter, Experiment Designer, Result Checker |
| 2 | Bioinformatics Pipeline | 5 | Data Inspector, QC Agent, Aligner Planner, Stats Agent, Interpreter |
| 3 | Climate Data Explorer | 5 | Data Fetcher Planner, Cleaner, Trend Analyst, Visualizer, Narrator |
| 4 | Math Problem Solver | 5 | Problem Parser, Strategy Picker, Calculator, Verifier, Explainer |
| 5 | Physics Simulation Planner | 5 | Model Builder, Numerics Chooser, Code Writer, Validation Agent, Plot Planner |
| 6 | Web Data Collector | 5 | Policy Checker, Selector Designer, Scraper Writer, Rate Limiter, Data Validator |
| 7 | AutoML Assistant | 5 | Problem Framer, Feature Engineer, Model Selector, Evaluator, Report Writer |
| 8 | Astronomy Observation Planner | 5 | Target Selector, Visibility Calculator, Equipment Advisor, Weather Agent, Log Template Writer |
| 9 | Chemistry Lab Notebook | 5 | Protocol Writer, Safety Officer, Calculation Agent, Data Table Designer, Error Analyst |
| 10 | Algorithm Benchmark Lab | 5 | Spec Writer, Implementer, Benchmark Designer, Analyzer, Reporter |
| 11 | Geospatial Analysis | 5 | Data Planner, Constraint Modeler, Scorer, Map Planner, Recommender |

Full per-agent instructions are in [AGENTS.md](AGENTS.md).

Each app uses one of two data-flow patterns (see `common/flow.py`):
`sequential` (each agent builds on the previous) or `fanout` (a planner, parallel specialists, then a merger).

## License

MIT
