"""Core business logic for the starter project."""


def greet(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    clean_name = name.strip() or "there"
    return f"Hello, {clean_name}!"
