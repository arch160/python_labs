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