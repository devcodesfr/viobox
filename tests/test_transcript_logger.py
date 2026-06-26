"""Tests for transcript formatting and logging."""

from app.models import ConversationTurn
from app.transcripts.formatter import format_turn
from app.transcripts.logger import write_transcript


def test_format_turn_uses_speaker_and_text() -> None:
    turn = ConversationTurn(speaker="Patient", text="Hello there.")

    assert format_turn(turn) == "Patient: Hello there."


def test_write_transcript_creates_text_file(tmp_path) -> None:
    path = tmp_path / "transcript.txt"
    turns = [ConversationTurn(speaker="Patient", text="Hi.")]

    write_transcript(path, turns)

    assert path.read_text(encoding="utf-8") == "Patient: Hi.\n"
