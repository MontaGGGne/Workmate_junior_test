from .report import Report
from .payout_report import PayoutReport


def get_report(name: str) -> Report:
    if name == "payout":
        return PayoutReport()
    raise ValueError(f"Unknown report type: '{name}'")