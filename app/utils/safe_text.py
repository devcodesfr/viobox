"""Text safety helpers."""


def single_line(text: str) -> str:
    return " ".join(text.split())
