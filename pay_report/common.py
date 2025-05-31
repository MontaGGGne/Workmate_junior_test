from typing import Optional

RATE_KEYS = {"hourly_rate", "rate", "salary"}


def find_rate_key(row: dict) -> Optional[str]:
    for key in RATE_KEYS:
        if key in row:
            return key
    return None