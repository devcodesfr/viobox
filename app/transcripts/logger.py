"""Transcript logging helpers."""

from __future__ import annotations

from pathlib import Path

from app.models import ConversationTurn
from app.transcripts.formatter import format_turn


def write_transcript(path: Path, turns: list[ConversationTurn]) -> Path:
    """Write a plain-text transcript for manual review."""

    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [format_turn(turn) for turn in turns]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
