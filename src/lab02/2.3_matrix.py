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
