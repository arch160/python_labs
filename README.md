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