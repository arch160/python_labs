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
