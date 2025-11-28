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
