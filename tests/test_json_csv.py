import pytest
from pathlib import Path
import json
import csv
from src.lab05.json_to_csv import json_to_csv
from src.lab05.csv_to_json import csv_to_json


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


def test_json_to_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")


def test_csv_to_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "output.json")


def test_json_to_csv_empty_file(tmp_path: Path):
    empty_json = tmp_path / "empty.json"
    empty_json.write_text("", encoding="utf-8")
    output_csv = tmp_path / "output.csv"

    with pytest.raises((ValueError, json.JSONDecodeError)):
        json_to_csv(str(empty_json), str(output_csv))


def test_json_to_csv_invalid_json(tmp_path: Path):
    invalid_json = tmp_path / "invalid.json"
    invalid_json.write_text("{invalid json}", encoding="utf-8")
    output_csv = tmp_path / "output.csv"

    with pytest.raises((ValueError, json.JSONDecodeError)):
        json_to_csv(str(invalid_json), str(output_csv))


def test_csv_to_json_empty_file(tmp_path: Path):
    empty_csv = tmp_path / "empty.csv"
    empty_csv.write_text("", encoding="utf-8")
    output_json = tmp_path / "output.json"

    csv_to_json(str(empty_csv), str(output_json))
    
    assert output_json.exists()
    with output_json.open(encoding="utf-8") as f:
        data = json.load(f)
    assert data == []


def test_csv_to_json_invalid_csv(tmp_path: Path):
    invalid_csv = tmp_path / "invalid.csv"
    invalid_csv.write_text("name,age\nAlice,22,extra\nBob", encoding="utf-8")
    output_json = tmp_path / "output.json"

    csv_to_json(str(invalid_csv), str(output_json))
    
    assert output_json.exists()
    with output_json.open(encoding="utf-8") as f:
        data = json.load(f)


def test_csv_to_json_malformed_csv(tmp_path: Path):
    malformed_csv = tmp_path / "malformed.csv"
    malformed_csv.write_text("name,age\nAlice\nBob,30", encoding="utf-8")
    output_json = tmp_path / "output.json"

    csv_to_json(str(malformed_csv), str(output_json))
    
    assert output_json.exists()
    with output_json.open(encoding="utf-8") as f:
        data = json.load(f)