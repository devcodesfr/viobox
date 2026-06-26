"""Transcript formatting helpers."""

from app.models import ConversationTurn


def format_turn(turn: ConversationTurn) -> str:
    speaker = turn.speaker.strip() or "Unknown"
    text = turn.text.strip()
    return f"{speaker}: {text}"
