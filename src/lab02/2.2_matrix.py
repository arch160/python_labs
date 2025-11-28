def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    row = len(mat[0])
    for row1 in mat:
        if len(row1) != row:
            return "ValueError"
    return [sum(r) for r in mat]


t = [[1, 2, 3], [4, 5, 6]]
a = [[-1, 1], [10, -10]]
b = [[0, 0], [0, 0]]
c = [[1, 2], [3]]
print(row_sums(t))
print(row_sums(a))
print(row_sums(b))
print(row_sums(c))
