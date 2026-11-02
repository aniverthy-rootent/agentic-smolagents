"""Climate Data Explorer

Task: Analyze 30 years of regional temperature data.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'climate_data'
TITLE = 'Climate Data Explorer'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Analyze 30 years of regional temperature data.'

# (key, role, instruction)
AGENTS = [
    ('data_fetcher_planner', 'Data Fetcher Planner', 'Define data sources.'),
    ('cleaner', 'Cleaner', 'Clean series.'),
    ('trend_analyst', 'Trend Analyst', 'Fit trends.'),
    ('visualizer', 'Visualizer', 'Plan charts.'),
    ('narrator', 'Narrator', 'Write findings.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
