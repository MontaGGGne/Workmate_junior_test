from typing import List, Dict, Any
from .report import Report
from .common import find_rate_key


class PayoutReport(Report):
    def generate(self, data: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        result = []

        for row in data:
            rate_key = find_rate_key(row)
            if not rate_key:
                raise ValueError("Missing salary/rate column in row")

            try:
                hours = float(row["hours_worked"])
                rate = float(row[rate_key])
                payout = hours * rate
            except (KeyError, ValueError):
                raise ValueError(f"Invalid numeric data in row: {row}")

            result.append({
                "id": row.get("id", ""),
                "name": row.get("name", ""),
                "department": row.get("department", ""),
                "payout": payout
            })

        return result