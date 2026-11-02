"""Web Data Collector

Task: Collect public product prices from three shops (respect robots.txt).
Framework: smolagents (Hugging Face)
"""
from runtime import run_app

SLUG = 'web_data_scraper'
TITLE = 'Web Data Collector'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Collect public product prices from three shops (respect robots.txt).'

# (key, role, instruction)
AGENTS = [
    ('policy_checker', 'Policy Checker', 'Check robots and terms.'),
    ('selector_designer', 'Selector Designer', 'Design selectors.'),
    ('scraper_writer', 'Scraper Writer', 'Write code.'),
    ('rate_limiter', 'Rate Limiter', 'Throttle plan.'),
    ('data_validator', 'Data Validator', 'Validate output.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
