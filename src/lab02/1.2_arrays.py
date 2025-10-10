def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if not nums:
        return 'ValueError'
    return sorted(set(nums))
t = [3, 1, 2, 1, 3]
print(unique_sorted(t))