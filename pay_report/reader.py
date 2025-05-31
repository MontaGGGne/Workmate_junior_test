from typing import List, Dict


def parse_csv(content: str) -> List[Dict[str, str]]:
    lines = [line.strip() for line in content.strip().split('\n') if line.strip()]
    headers = lines[0].split(',')
    rows = []
    for line in lines[1:]:
        values = line.split(',')
        row = dict(zip(headers, values))
        rows.append(row)
    return rows


def read_csv_file(filename: str) -> List[Dict[str, str]]:
    with open(filename, encoding="utf-8") as f:
        content = f.read()
    return parse_csv(content)