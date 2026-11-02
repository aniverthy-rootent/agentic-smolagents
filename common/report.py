"""Pretty-print an application run."""


def show(title: str, result: dict) -> None:
    print(f"=== {title} ===")
    for key, text in result.items():
        print(f"\n[{key}]\n{text}")
