"""Simple call state container."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CallState:
    scenario_id: str
    turn_count: int = 0
    goal_achieved: bool = False
    notes: list[str] = field(default_factory=list)

    def record_turn(self) -> None:
        self.turn_count += 1
