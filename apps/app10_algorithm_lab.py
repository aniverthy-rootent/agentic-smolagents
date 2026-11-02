"""Algorithm Benchmark Lab

Task: Compare quicksort, mergesort and heapsort.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'algorithm_lab'
TITLE = 'Algorithm Benchmark Lab'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Compare quicksort, mergesort and heapsort.'

# (key, role, instruction)
AGENTS = [
    ('spec_writer', 'Spec Writer', 'Define experiment.'),
    ('implementer', 'Implementer', 'Write implementations.'),
    ('benchmark_designer', 'Benchmark Designer', 'Design inputs.'),
    ('analyzer', 'Analyzer', 'Analyze complexity.'),
    ('reporter', 'Reporter', 'Write findings.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
