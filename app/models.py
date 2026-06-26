"""Shared lightweight models."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ConversationTurn:
    speaker: str
    text: str
    timestamp: datetime | None = None


@dataclass(frozen=True)
class CallSummary:
    scenario_id: str
    status: str
    transcript_path: str | None = None
    recording_path: str | None = None
