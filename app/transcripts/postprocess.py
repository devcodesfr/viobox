"""Transcript cleanup placeholders."""


def normalize_transcript_text(text: str) -> str:
    return "\n".join(line.strip() for line in text.strip().splitlines())
