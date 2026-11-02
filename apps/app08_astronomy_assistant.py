"""Astronomy Observation Planner

Task: Plan a stargazing night at 40N latitude in October.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'astronomy_assistant'
TITLE = 'Astronomy Observation Planner'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Plan a stargazing night at 40N latitude in October.'

# (key, role, instruction)
AGENTS = [
    ('target_selector', 'Target Selector', 'Pick targets.'),
    ('visibility_calculator', 'Visibility Calculator', 'Compute visibility.'),
    ('equipment_advisor', 'Equipment Advisor', 'Advise equipment.'),
    ('weather_agent', 'Weather Agent', 'Weather planning.'),
    ('log_template_writer', 'Log Template Writer', 'Observation log.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
