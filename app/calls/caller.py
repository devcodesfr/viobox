"""Placeholder for future Twilio outbound call logic."""

from app.config import Settings, validate_target_number


def start_call(target_number: str, settings: Settings | None = None) -> None:
    """Validate the target number, then stop before any real call is made."""

    validate_target_number(target_number, settings)
    raise NotImplementedError("Twilio call logic is intentionally not implemented yet.")
