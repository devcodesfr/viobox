"""Tests for scenario definitions."""

from app.scenarios.registry import get_scenario, list_scenarios


def test_there_are_at_least_ten_scenarios() -> None:
    assert len(list_scenarios()) >= 10


def test_scenario_ids_are_unique() -> None:
    scenario_ids = [scenario.id for scenario in list_scenarios()]

    assert len(scenario_ids) == len(set(scenario_ids))


def test_get_scenario_returns_requested_scenario() -> None:
    scenario = get_scenario("appointment_basic")

    assert scenario.id == "appointment_basic"
    assert scenario.persona.name == "Jordan Smith"
