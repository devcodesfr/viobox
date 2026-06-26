"""Recording placeholders for future Twilio downloads."""


def recording_filename(call_id: str, extension: str = "wav") -> str:
    safe_call_id = call_id.replace("/", "_").replace("\\", "_")
    return f"{safe_call_id}.{extension.lstrip('.')}"
