"""AutoML Assistant

Task: Build a churn prediction baseline.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'automl_assistant'
TITLE = 'AutoML Assistant'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Build a churn prediction baseline.'

# (key, role, instruction)
AGENTS = [
    ('problem_framer', 'Problem Framer', 'Define target.'),
    ('feature_engineer', 'Feature Engineer', 'Propose features.'),
    ('model_selector', 'Model Selector', 'Pick models.'),
    ('evaluator', 'Evaluator', 'Choose metrics.'),
    ('report_writer', 'Report Writer', 'Summarize.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
