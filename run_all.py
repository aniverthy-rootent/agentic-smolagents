"""Run every application in this repository."""
import importlib
import pkgutil

import apps
from common.report import show


def main() -> None:
    for mod in sorted(m.name for m in pkgutil.iter_modules(apps.__path__)):
        app = importlib.import_module(f"apps.{mod}")
        show(app.TITLE, app.main())
        print("\n" + "-" * 60)


if __name__ == "__main__":
    main()
