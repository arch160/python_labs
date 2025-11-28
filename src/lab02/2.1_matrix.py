def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []

    row = len(mat[0])
    for row1 in mat:
        if len(row1) != row:
            return "ValueError"
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
