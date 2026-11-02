"""Paper Replication

Task: Plan the replication of a small CNN image-classification paper.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'paper_replication'
TITLE = 'Paper Replication'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Plan the replication of a small CNN image-classification paper.'

# (key, role, instruction)
AGENTS = [
    ('paper_reader', 'Paper Reader', 'Extract method.'),
    ('environment_planner', 'Environment Planner', 'Plan dependencies.'),
    ('code_drafter', 'Code Drafter', 'Draft the code.'),
    ('experiment_designer', 'Experiment Designer', 'Design runs.'),
    ('result_checker', 'Result Checker', 'Define success criteria.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
