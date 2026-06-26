"""Manual-first bug suggestion placeholder."""


def suggest_quality_issues(transcript_text: str) -> list[str]:
    """Return simple heuristic suggestions for later manual review."""

    if not transcript_text.strip():
        return ["Transcript is empty or missing."]
    return []
