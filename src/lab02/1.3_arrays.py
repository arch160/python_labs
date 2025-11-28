def flatten(mat: list[list | tuple]) -> list:
    res = []
    for r in mat:
        if not isinstance(r, (list, tuple)):
            return "TypeError"
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
