import json
from pathlib import Path
from typing import List

from src.lab08.models import Student


def students_to_json(students: List[Student], path: str | Path) -> None:
    output_path = Path(path)
    data = [student.to_dict() for student in students]
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> List[Student]:
    input_path = Path(path)
    if not input_path.exists():
        raise FileNotFoundError(f"Файл не найден: {input_path}")
    
    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    
    if not isinstance(data, list):
        raise ValueError("Ожидается список студентов в JSON")
    
    return [Student.from_dict(item) for item in data]


if __name__ == "__main__":
    input_path = Path(__file__).parent.parent.parent / "data" / "lab08" / "students_input.json"
    
    try:
        print(f"Загрузка из входного файла: {input_path}")
        students = students_from_json(input_path)
        
        print("\nЗагруженные студенты:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")
        
        output_path = Path(__file__).parent.parent.parent / "data" / "lab08" / "students_output.json"
        print(f"\nСохранение в выходной файл: {output_path}")
        students_to_json(students, output_path)
        
        print(f"\nПроверка загрузки из выходного файла:")
        loaded_students = students_from_json(output_path)
        for i, student in enumerate(loaded_students, 1):
            print(f"{i}. {student}")
        
        print(f"\nРезультат: загружено {len(students)}, сохранено {len(loaded_students)}")
        
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        print("Создайте файл data/lab08/students_input.json с тестовыми данными")
    except Exception as e:
        print(f"Ошибка: {e}")