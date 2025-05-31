import pytest
from ..pay_report.payout_report import PayoutReport


def test_payout_report_with_valid_data():
    data = [
        {"id": "1", "name": "Alice", "department": "HR", "hours_worked": "100", "salary": "50"},
        {"id": "2", "name": "Bob", "department": "Dev", "hours_worked": "120", "rate": "60"},
        {"id": "3", "name": "Carol", "department": "QA", "hours_worked": "160", "hourly_rate": "40"},
    ]

    report = PayoutReport()
    result = report.generate(data)

    assert result == [
        {"id": "1", "name": "Alice", "department": "HR", "payout": 5000.0},
        {"id": "2", "name": "Bob", "department": "Dev", "payout": 7200.0},
        {"id": "3", "name": "Carol", "department": "QA", "payout": 6400.0},
    ]


def test_payout_report_missing_rate():
    data = [{"id": "1", "name": "Alice", "department": "HR", "hours_worked": "100"}]
    report = PayoutReport()
    with pytest.raises(ValueError):
        report.generate(data)


def test_payout_report_invalid_numeric():
    data = [{"id": "1", "name": "Alice", "department": "HR", "hours_worked": "abc", "rate": "xyz"}]
    report = PayoutReport()
    with pytest.raises(ValueError):
        report.generate(data)