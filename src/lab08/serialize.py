import json
from pathlib import Path
from typing import List

from src.lab08.models import Student


def students_to_json(students: List[Student], path: str | Path) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    data = [student.to_dict() for student in students]
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> List[Student]:
    input_path = Path(path)
    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    
    return [Student.from_dict(item) for item in data]

if __name__ == "__main__":
    students_input = students_from_json("data/lab08/students_input.json")
    
    for student in students_input:
        print(student)
    
    students_to_json(students_input, "data/lab08/students_output.json")