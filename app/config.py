"""Configuration helpers for Viobox."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Environment-backed settings used by local scripts and future webhooks."""

    assessment_test_number: str = ""
    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    twilio_from_number: str = ""
    openai_api_key: str = ""
    app_base_url: str = "http://localhost:8000"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            assessment_test_number=os.getenv("ASSESSMENT_TEST_NUMBER", "").strip(),
            twilio_account_sid=os.getenv("TWILIO_ACCOUNT_SID", "").strip(),
            twilio_auth_token=os.getenv("TWILIO_AUTH_TOKEN", "").strip(),
            twilio_from_number=os.getenv("TWILIO_FROM_NUMBER", "").strip(),
            openai_api_key=os.getenv("OPENAI_API_KEY", "").strip(),
            app_base_url=os.getenv("APP_BASE_URL", "http://localhost:8000").strip(),
        )


def validate_target_number(target_number: str, settings: Settings | None = None) -> bool:
    """Allow calls only to the configured assessment test number."""

    active_settings = settings or Settings.from_env()
    allowed_number = active_settings.assessment_test_number.strip()
    requested_number = target_number.strip()

    if not allowed_number:
        raise ValueError("ASSESSMENT_TEST_NUMBER is not configured.")

    if requested_number != allowed_number:
        raise ValueError("Refusing to call any number except ASSESSMENT_TEST_NUMBER.")

    return True
