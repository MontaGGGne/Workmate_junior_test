import argparse
import json
import sys
from .report_factory import get_report
from .reader import read_csv_file


def main():
    parser = argparse.ArgumentParser(description="Payroll Report Generator")
    parser.add_argument("files", nargs='+', help="CSV files with employee data")
    parser.add_argument("--report", required=True, help="Type of report to generate")
    args = parser.parse_args()

    try:
        all_data = []
        for file in args.files:
            all_data.extend(read_csv_file(file))

        report = get_report(args.report)
        result = report.generate(all_data)

        print(json.dumps(result, indent=2))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()