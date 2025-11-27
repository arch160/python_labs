import pytest
import os
import sys
from pathlib import Path
import json
import csv

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '..', 'src')
sys.path.insert(0, src_path)

from lab05.json_to_csv import json_to_csv
from lab05.csv_to_json import csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    
    csv_content = "name,age\nAlice,22\nBob,25"
    src.write_text(csv_content, encoding="utf-8")
    
    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(json.load(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())