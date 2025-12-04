# Лабораторная работа № 8

## Models

```python
from dataclasses import dataclass
from datetime import date, datetime 

DATE_FORMAT = "%Y-%m-%d"
GPA_MIN = 0
GPA_MAX = 5

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    @staticmethod
    def _validate_birthdate(birthdate: str) -> date:
        try:
            return datetime.strptime(birthdate, DATE_FORMAT).date()
        except ValueError:
            raise ValueError("Некорректный формат даты")

    @staticmethod
    def _validate_gpa(value: float) -> float:
        try:
            gpa_value = float(value)
        except (TypeError, ValueError):
            raise ValueError("Средний балл должен быть числом")

        if not GPA_MIN <= gpa_value <= GPA_MAX:
            raise ValueError("Средний балл должен быть в диапазоне от 0 до 5")
        return gpa_value
    
    def __post_init__(self) -> None:
        self._birthdate_dt = Student._validate_birthdate(self.birthdate)
        self.gpa = Student._validate_gpa(self.gpa)

    def age(self) -> int:
        today = date.today()
        years = today.year - self._birthdate_dt.year
        if (today.month, today.day) < (self._birthdate_dt.month, self._birthdate_dt.day):
            years -= 1
        return years

    def to_dict(self):
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"],
        )

    def __str__(self) -> str:
        return f"{self.fio} ({self.group}), {self.age()} лет, GPA {self.gpa:.2f}"
```

## Serialize

```python
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

    input_file = Path(__file__).parent.parent.parent / "data" / "lab08" / "students_input.json"
    output_file = Path(__file__).parent.parent.parent / "data" / "lab08" / "students_output.json"
    
    students = students_from_json(input_file)
    
    for student in students:
        print(student)
    
    students_to_json(students, output_file)
```

## Файлы students_input и students_output:
![1](../../images/lab08/1.png)

## Вывод:
![2](../../images/lab08/2.png)