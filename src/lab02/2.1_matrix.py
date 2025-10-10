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