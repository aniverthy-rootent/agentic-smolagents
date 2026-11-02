"""Physics Simulation Planner

Task: Simulate a damped pendulum.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'physics_simulator'
TITLE = 'Physics Simulation Planner'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Simulate a damped pendulum.'

# (key, role, instruction)
AGENTS = [
    ('model_builder', 'Model Builder', 'Write equations.'),
    ('numerics_chooser', 'Numerics Chooser', 'Choose integrator.'),
    ('code_writer', 'Code Writer', 'Write code.'),
    ('validation_agent', 'Validation Agent', 'Define checks.'),
    ('plot_planner', 'Plot Planner', 'Plan plots.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
