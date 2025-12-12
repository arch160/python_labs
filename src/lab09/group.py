import csv
from pathlib import Path
from typing import List
from src.lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                f.write("fio,birthdate,group,gpa\n")
    
    def _read_all(self):
        if not self.path.exists():
            return []
        with open(self.path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _write_all(self, rows):
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self):
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                student = Student.from_dict(row)
                students.append(student)
            except:
                continue
        return students
    
    def add(self, student: Student):
        rows = self._read_all()
        
        student_dict = student.to_dict()
        for row in rows:
            if (row['fio'] == student_dict['fio'] and
                row['birthdate'] == student_dict['birthdate'] and
                row['group'] == student_dict['group'] and
                float(row['gpa']) == float(student_dict['gpa'])):
                raise ValueError(f"Такой студент уже существует: {student.fio}")
        
        rows.append(student_dict)
        self._write_all(rows)
    
    def find(self, substr: str):
        rows = self._read_all()
        found = [row for row in rows if substr.lower() in row['fio'].lower()]
        students = []
        for row in found:
            try:
                student = Student.from_dict(row)
                students.append(student)
            except:
                continue
        return students
    
    def remove(self, fio: str):
        rows = self._read_all()
        new_rows = [row for row in rows if row['fio'] != fio]
        if len(new_rows) < len(rows):
            self._write_all(new_rows)
            return True
        return False
    
    def update(self, fio: str, **fields):
        rows = self._read_all()
        updated = False
        
        for i, row in enumerate(rows):
            if row['fio'] == fio:
                updated = True
                
                temp_row = row.copy()
                for key, value in fields.items():
                    if key in ["fio", "birthdate", "group", "gpa"]:
                        if key == 'gpa':
                            value = str(float(value))
                        temp_row[key] = str(value)
                
                for j, other_row in enumerate(rows):
                    if i != j:
                        if (temp_row['fio'] == other_row['fio'] and
                            temp_row['birthdate'] == other_row['birthdate'] and
                            temp_row['group'] == other_row['group'] and
                            float(temp_row['gpa']) == float(other_row['gpa'])):
                            raise ValueError(f"После обновления будет дубликат студента: {temp_row['fio']}")
                
                for key, value in fields.items():
                    if key in ["fio", "birthdate", "group", "gpa"]:
                        if key == 'gpa':
                            value = str(float(value))
                        rows[i][key] = str(value)
        
        if not updated:
            raise ValueError(f"Студент {fio} не найден")
        
        self._write_all(rows)