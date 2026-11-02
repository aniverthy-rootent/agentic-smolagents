"""Geospatial Analysis

Task: Find the best site for a new EV charging hub.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'geospatial_analysis'
TITLE = 'Geospatial Analysis'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Find the best site for a new EV charging hub.'

# (key, role, instruction)
AGENTS = [
    ('data_planner', 'Data Planner', 'Choose layers.'),
    ('constraint_modeler', 'Constraint Modeler', 'Define constraints.'),
    ('scorer', 'Scorer', 'Score locations.'),
    ('map_planner', 'Map Planner', 'Plan maps.'),
    ('recommender', 'Recommender', 'Recommend sites.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
