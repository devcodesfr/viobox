"""Tests for safe target-number validation."""

import pytest

from app.config import Settings, validate_target_number


def test_validate_target_number_accepts_configured_number() -> None:
    settings = Settings(assessment_test_number="+15555550123")

    assert validate_target_number("+15555550123", settings) is True


def test_validate_target_number_rejects_other_number() -> None:
    settings = Settings(assessment_test_number="+15555550123")

    with pytest.raises(ValueError):
        validate_target_number("+15555559999", settings)
