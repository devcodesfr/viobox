"""Scenario registry helpers."""

from app.scenarios.base import Scenario
from app.scenarios.pgai_healthcare import SCENARIOS


def list_scenarios() -> tuple[Scenario, ...]:
    return SCENARIOS


def get_scenario(scenario_id: str) -> Scenario:
    for scenario in SCENARIOS:
        if scenario.id == scenario_id:
            return scenario

    raise KeyError(f"Unknown scenario: {scenario_id}")
