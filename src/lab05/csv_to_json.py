import json
import csv
from pathlib import Path
import sys

current_file = Path(__file__)
print(f"Текущий файл: {current_file}")

parent_dir = current_file.parent.parent
sys.path.append(str(parent_dir))


def csv_to_json(csv_path: str, json_path: str) -> None:
    encoding = 'utf-8'
    input_path = Path(csv_path)
    output_path = Path(json_path)
    
    if not input_path.exists():
        raise FileNotFoundError('Пожалуйста, проверьте путь к файлу')
    if input_path.suffix.lower() != '.csv':
        raise ValueError('Проверьте расширение файла')
    
    data = []
    with open(input_path, 'r', encoding=encoding, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    with open(output_path, 'w', encoding=encoding, newline='') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
        print('Конвертация прошла успешно')
        print(f'Всего записей конвертировано: {len(data)}')


csv_to_json('src/data/file1.csv', 'src/data/file1.json')