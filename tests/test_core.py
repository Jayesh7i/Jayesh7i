from jayesh7i.core import greet


def test_greet_with_name() -> None:
    assert greet("Jayesh") == "Hello, Jayesh!"


def test_greet_with_blank_name() -> None:
    assert greet("   ") == "Hello, there!"
