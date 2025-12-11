from dataclasses import dataclass
from datetime import date, datetime 

DATE_FORMAT = "%Y-%m-%d"
GPA_MIN = 0
GPA_MAX = 5

@dataclass
class Student:
    fio: str
    birthdate: str  # хранится как строка "2003-10-10"
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
        # ИСПРАВЛЕНО: используем self.birthdate
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
            "gpa": self.gpa
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