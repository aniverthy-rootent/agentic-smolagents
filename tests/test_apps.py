import importlib
import pkgutil

import pytest

import apps

MODULES = sorted(m.name for m in pkgutil.iter_modules(apps.__path__))


def test_eleven_apps():
    assert len(MODULES) == 11


@pytest.mark.parametrize("name", MODULES)
def test_app_runs_offline(name):
    app = importlib.import_module(f"apps.{name}")
    assert 5 <= len(app.AGENTS) <= 6
    result = app.main()
    assert list(result) == [a[0] for a in app.AGENTS]
    assert all(isinstance(v, str) and v.strip() for v in result.values())
