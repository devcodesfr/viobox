"""Tests for simple conversation rules."""

from app.conversation.rules import should_wrap_up


def test_should_wrap_up_when_goal_is_achieved() -> None:
    assert should_wrap_up(turn_count=2, max_turns=12, goal_achieved=True) is True


def test_should_wrap_up_when_max_turns_reached() -> None:
    assert should_wrap_up(turn_count=12, max_turns=12, goal_achieved=False) is True


def test_should_continue_before_goal_or_limit() -> None:
    assert should_wrap_up(turn_count=3, max_turns=12, goal_achieved=False) is False
