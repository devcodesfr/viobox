"""Simple scripted response rules."""


def should_wrap_up(turn_count: int, max_turns: int, goal_achieved: bool) -> bool:
    """Decide whether the patient should start ending the call."""

    return goal_achieved or turn_count >= max_turns
