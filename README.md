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
print(min_max(t))
```
![min_max](./images/lab02/1.1_arrays.png)

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if not nums:
        return 'ValueError'
    return sorted(set(nums))
t = [3, 1, 2, 1, 3]
print(unique_sorted(t))
```

![unique_sorted](./images/lab02/1.2_arrays.png)

```python
def flatten(mat: list[list | tuple]) -> list:
   if not mat:
      return [] 
   
   row = len(mat[0])
   for row1 in mat:
    if len(row1) != row:
         return 'ValueError'
    res = []
    for row1 in mat:
        res.extend(row1)
    return res
t = [[1, 2], [3, 4]]
print(flatten(t))
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
t = [[1],[2],[3]]
res = transpose(t)
print(res)
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
res = row_sums(t)
print(res)
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
res = col_sums(t)
print(res)
```
![col_sums](./images/lab02/2.3_matrix.png)

## Задание 3

```python
def format_record(rec: tuple[str, str, float]) -> str:
    fio, gr, gpa = rec
    fio2 = ' '.join(fio.split()).split()
    fam = fio2[0]

    ini = []
    for i in range(1, len(fio2)):
        if i <= 2:
            ini.append(f"{fio2[i][0]}.")
    res = f"{fam} {''.join(ini)}, гр. {gr}, GPA {gpa:.2f}"
    return res
t = ('Иванов Иван Иванович', "IKBO-12", 5.0)
print(format_record(t))
```

![Записи](./images/lab02/typles.png)
