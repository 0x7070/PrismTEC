from datetime import datetime, timezone, timedelta

def generate_iso_timestamp():
    """Generates an ISO8601 timestamp for the current time

    Returns:
        str: ISO8601 timestamp
        >>> `2026-02-03T15:33:16.330169+00:00`
    """
    return datetime.now(timezone.utc).isoformat()