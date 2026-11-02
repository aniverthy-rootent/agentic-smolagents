"""Bioinformatics Pipeline

Task: Outline analysis of RNA-seq differential expression.
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'bioinformatics_pipeline'
TITLE = 'Bioinformatics Pipeline'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Outline analysis of RNA-seq differential expression.'

# (key, role, instruction)
AGENTS = [
    ('data_inspector', 'Data Inspector', 'Inspect inputs.'),
    ('qc_agent', 'QC Agent', 'Define quality control.'),
    ('aligner_planner', 'Aligner Planner', 'Plan alignment.'),
    ('stats_agent', 'Stats Agent', 'Differential analysis.'),
    ('interpreter', 'Interpreter', 'Interpret results.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
