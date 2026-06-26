"""Placeholder TwiML helpers."""


def build_placeholder_response(message: str) -> str:
    """Return a tiny TwiML response for future webhook tests."""

    escaped_message = message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f"<Response><Say>{escaped_message}</Say></Response>"
