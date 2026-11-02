"""Chemistry Lab Notebook

Task: Plan titration of acetic acid with NaOH.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'chemistry_lab'
TITLE = 'Chemistry Lab Notebook'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Plan titration of acetic acid with NaOH.'

# (key, role, instruction)
AGENTS = [
    ('protocol_writer', 'Protocol Writer', 'Write protocol.'),
    ('safety_officer', 'Safety Officer', 'List hazards.'),
    ('calculation_agent', 'Calculation Agent', 'Compute amounts.'),
    ('data_table_designer', 'Data Table Designer', 'Plan tables.'),
    ('error_analyst', 'Error Analyst', 'Error sources.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
