# Лабораторная работа № 1

## Задание 1
![Приветствие](./images/lab01/01.png)

## Задание 2
![Вещественные числа](./images/lab01/02.png)

## Задание 3 
![Цены](./images/lab01/03.png)

## Задание 4
![Время](./images/lab01/04.png)

## Задание 5 
![ФИО](./images/lab01/05.png)


# Лабораторная работа № 2

## Задание 1

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return 'ValueError'
    return (min(nums), max(nums))
t = [3, -1, 5, 5, 0]
m = [42]
n = [-5, -2, -9]
b = []
a = [1.5, 2, 2.0, -3.1]
print(min_max(t))
print(min_max(m))
print(min_max(n))
print(min_max(b))
print(min_max(a))
```
![min_max](./images/lab02/1.1_arrays.png)

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if not nums:
        return []
    return sorted(set(nums))
t = [3, 1, 2, 1, 3]
c = []
a = [-1, -1, 0, 2, 2]
b = [1.0, 1, 2.5, 2.5, 0]
print(unique_sorted(t))
print(unique_sorted(c))
print(unique_sorted(a))
print(unique_sorted(b))
```

![unique_sorted](./images/lab02/1.2_arrays.png)

```python
def flatten(mat: list[list | tuple]) -> list:
    res = []
    for r in mat:
        if not isinstance(r, (list, tuple)):
            return 'TypeError'
        res.extend(r)
    return res
t = [[1, 2], [3, 4]]
a = [[1, 2], (3, 4, 5)]
b = [[1], [], [2, 3]]
c = [[1, 2], "ab"]
print(flatten(t))
print(flatten(a))
print(flatten(b))
print(flatten(c))
```
![flatten](./images/lab02/1.3_arrays.png)

## Задание 2

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
      return []
    
    row = len(mat[0])
    for row1 in mat:
        if len(row1) != row:
         return 'ValueError'
    return [[mat[q][w] for q in range(len(mat))] for w in range(row)]
t = [[1, 2, 3]]
a = [[1], [2], [3]]
b = [[1, 2], [3, 4]]
c = []
d = [[1, 2], [3]]
print(transpose(t))
print(transpose(a))
print(transpose(b))
print(transpose(c))
print(transpose(d))
```
![transpose](./images/lab02/2.1_matrix.png)

```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
      return []
    
    row = len(mat[0])
    for row1 in mat:
        if len(row1) != row:
         return 'ValueError'
    return [sum(r) for r in mat]
t = [[1, 2, 3], [4, 5, 6]]
a = [[-1, 1], [10, -10]]
b = [[0, 0], [0, 0]]
c = [[1, 2], [3]]
print(row_sums(t))
print(row_sums(a))
print(row_sums(b))
print(row_sums(c))
```
![row_sums](./images/lab02/2.2_matrix.png)

```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
      return []
    
    row = len(mat[0])
    for row1 in mat:
        if len(row1) != row:
         return 'ValueError'
    return [sum(r) for r in zip(*mat)]
t = [[1, 2, 3], [4, 5, 6]]
a = [[-1, 1], [10, -10]]
b = [[0, 0], [0, 0]]
c = [[1, 2], [3]]
print(col_sums(t))
print(col_sums(a))
print(col_sums(b))
print(col_sums(c))
```
![col_sums](./images/lab02/2.3_matrix.png)

## Задание 3

```python
def format_record(rec: tuple[str, str, float]) -> str:
    try:
        fio, gr, gpa = rec
        fio2 = ' '.join(fio.split()).split()
        fam = fio2[0]

        if (fio not in rec) or (gr not in rec) or (gpa not in rec):
            return 'ValueError'

        ini = []
        for i in range(1, len(fio2)):
            if i <= 2:
                ini.append(f"{fio2[i][0]}.")
        res = f"{fam} {''.join(ini)}, гр. {gr}, GPA {gpa:.2f}"
        return res
    except:
       return 'ValueError'
t = ("Иванов Иван Иванович", "BIVT-25", 4.6)
a = ("Петров Пётр", "IKBO-12", 5.0)
b = ("Петров Пётр Петрович", "IKBO-12", 5.0)
c = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
d = (" ", "ABB-01")
print(format_record(t))
print(format_record(a))
print(format_record(b))
print(format_record(c))
print(format_record(d))
```

![Записи](./images/lab02/typles.png)


# Лабораторная работа № 3

## Задание 1

### Normalize

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    text = ' '.join(text.split())
    text = text.strip()
    return text
a = 'ПрИвЕт\nМИр\t'
b = "ёжик, Ёлка"
c = "Hello\r\nWorld"
d = "  двойные   пробелы  "
print(normalize(a))
print(normalize(b))
print(normalize(c))
print(normalize(d))
```
![normalize](./images/lab03/1.1_normalize.png)

### Tokenize

```python
import re

def tokenize(text: str) -> list[str]:
    t = r'[\w]+(?:-[\w]+)*'
    l = re.findall(t, text, re.UNICODE)
    return l

a = "привет мир"
b = "hello,world!!!"
c = "по-настоящему круто"
d = "2025 год"
e = "emoji 😀 не слово"
print(tokenize(a))
print(tokenize(b))
print(tokenize(c))
print(tokenize(d))
print(tokenize(e))
```

![tokenize](./images/lab03/1.2_tokenize.png)

### Count_freq + top_n
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = []
    for word in freq:
        count = freq[word]
        items.append((word, count))
    items.sort(key=lambda i: (-i[1], i[0]))
    return items[:n]


a = ["a","b","a","c","b","a"]
b = ["bb","aa","bb","aa","cc"]
print(count_freq(a))
print(count_freq(b))
print(top_n(count_freq(a)))
print(top_n(count_freq(b)))
```

![count_freq + top_n](./images/lab03/1.3-4_count_freq.png)

## Задание 2

### Задание B

```python
import sys
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    text = ' '.join(text.split())
    text = text.strip()
    return text

def tokenize(text: str) -> list[str]:
    t = r'[\w]+(?:-[\w]+)*'
    l = re.findall(t, text, re.UNICODE)
    return l

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = []
    for word in freq:
        count = freq[word]
        items.append((word, count))
    items.sort(key=lambda i: (-i[1], i[0]))
    return items[:n]

a =  "Привет, мир! Привет!!!"

nt = normalize(a)
allwords = tokenize(nt)
uw = count_freq(allwords)
top = top_n(uw, 5)

print(f'Всего слов: {len(allwords)}')
print(f"Уникальных слов: {len(uw)}")
print("Топ-5:")
for y in top:
    print(y[0] + ': ' + str(y[1]))
```

![Задание B.1](./images/lab03/2.1.1_text_stats.png)
![Задание B.2](./images/lab03/2.1.2_text_stats.png)


# Лабораторная работа № 4

## Функции, файл io_txt_csv.py: 
```python
from pathlib import Path
import csv
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализует текст: приводит к нижнему регистру, заменяет ё на е, убирает лишние пробелы"""
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    text = ' '.join(text.split())
    text = text.strip()
    return text

def tokenize(text: str) -> list[str]:
    """Разбивает текст на токены (слова)"""
    t = r'[\w]+(?:-[\w]+)*'
    l = re.findall(t, text, re.UNICODE)
    return l

def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоту каждого токена"""
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N самых частых токенов"""
    items = []
    for word in freq:
        count = freq[word]
        items.append((word, count))
    items.sort(key=lambda i: (-i[1], i[0]))
    return items[:n]

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текст из файла"""
    print(f"Читаю файл: {path}")
    p = Path(path)
    text = p.read_text(encoding=encoding)
    print(f"Прочитал {len(text)} символов")
    return text

def write_csv(rows: list[tuple | list], path: str | Path,
                header: tuple[str, ...] | None = None) -> None:
    """Записывает данные в CSV файл"""
    p = Path(path)

    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(f"ошибка лютая")
            
    with p.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)

        for row in rows:
            writer.writerow(row)
```

## Задание А
```python
from pathlib import Path
import sys

current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from io_txt_csv import normalize, tokenize, count_freq, top_n, read_text, write_csv

def main():
    current_file = Path(__file__)
    print(f"Текущий файл: {current_file}")

    input_path = current_file.parent / 'data' / 'input.txt'
    output_path = current_file.parent / 'data' / 'output.csv'

    print(f"Путь к входному файлу: {input_path}")
    print(f"Путь к выходному файлу: {output_path}")

    input_path.parent.mkdir(parents=True, exist_ok=True)
    input_path.write_text("Привет, мир! Привет!!!", encoding='utf-8')
    print(f"Создан/обновлен файл: {input_path}")

    result = read_text(input_path)
    print(f"Результат чтения: {result}")

    normalized_text = normalize(result)
    print(f"Нормализованный текст: {normalized_text}")

    tokens = tokenize(normalized_text)
    print(f"Токены: {tokens}")

    frequencies = count_freq(tokens)
    print(f"Частоты: {frequencies}")

    word_counts = top_n(frequencies, n=len(frequencies))
    print(f"Подсчет слов: {word_counts}")

    write_csv(word_counts, output_path, header=('word', 'count'))
    print(f"CSV файл создан: {output_path}")

if __name__ == "__main__":
    main()
```

## Задание B 
```python
from pathlib import Path
from io_txt_csv import normalize, tokenize, count_freq, top_n, read_text, write_csv

current_file = Path(__file__)
input_path = current_file.parent.parent / "src/data/input_test.txt"
output_path = current_file.parent.parent / "src/data/output.csv"

print(f"Текущий файл: {current_file}")
print(f"Входной файл: {input_path}")
print(f"Выходной файл: {output_path}")

input_path.parent.mkdir(parents=True, exist_ok=True)
if input_path.exists():
    input_path.unlink()
input_path.write_text("Привет", encoding="utf-8")
print(f"Создан пустой файл: {input_path}")

text = read_text(input_path, "utf-8")
print(f"Прочитано: '{text}' ({len(text)} символов)")

normalized_text = normalize(text)
tokens = tokenize(normalized_text)
frequencies = count_freq(tokens)

print(f"Токены: {tokens}")
print(f"Частоты: {frequencies}")

word_counts = top_n(frequencies, n=len(frequencies))
write_csv([[word, count] for word, count in word_counts], 
          output_path, header=('word', 'count'))
print(f"CSV создан: {output_path}")

print(f"Всего слов: {sum(frequencies.values())}")
print(f"Уникальных слов: {len(frequencies)}")

print("Топ 5 слов:")
top_5 = top_n(frequencies, n=5)
for i, (word, count) in enumerate(top_5, 1):
    print(f"  {i}. '{word}': {count}") if top_5 else print("  Нет слов")
```


## Тест кейсы к заданию А:
![1](./images/lab04/1.png)
![2](./images/lab04/2.png)

## Тест кейсы к заданию B
![3](./images/lab04/3.png)
![4](./images/lab04/4.png)
![5](./images/lab04/5.png)