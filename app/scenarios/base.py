"""Base scenario models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PatientPersona:
    name: str
    dob: str
    phone: str
    insurance: str
    pharmacy: str


@dataclass(frozen=True)
class Scenario:
    id: str
    title: str
    persona: PatientPersona
    goal: str
    opening_line: str
    facts: tuple[str, ...]
    success_criteria: tuple[str, ...]
    max_turns: int
    wrap_up_line: str
