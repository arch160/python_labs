import json
import csv
from pathlib import Path
import sys

current_file = Path(__file__)

parent_dir = current_file.parent.parent
sys.path.append(str(parent_dir))


def json_to_csv(
    json_path: str | Path, csv_path: str | Path, encoding: str = "utf-8"
) -> None:
    input_path = Path(json_path)
    output_path = Path(csv_path)

    if not input_path.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")

    with open(input_path, "r", encoding="utf-8-sig") as json_file:
        data = json.load(json_file)

    with open(output_path, "w", newline="", encoding=encoding) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Конвертировано {len(data)} записей")


if __name__ == "__main__":
    json_to_csv("src/data/file2.json", "src/data/file2.csv")
