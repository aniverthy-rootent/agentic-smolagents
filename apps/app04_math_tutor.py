"""Math Problem Solver

Task: Solve: integrate x * e^x from 0 to 1.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'math_tutor'
TITLE = 'Math Problem Solver'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Solve: integrate x * e^x from 0 to 1.'

# (key, role, instruction)
AGENTS = [
    ('problem_parser', 'Problem Parser', 'Restate.'),
    ('strategy_picker', 'Strategy Picker', 'Choose method.'),
    ('calculator', 'Calculator', 'Compute.'),
    ('verifier', 'Verifier', 'Verify result.'),
    ('explainer', 'Explainer', 'Explain steps.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
