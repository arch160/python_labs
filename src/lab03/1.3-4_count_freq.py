def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = []
    for word in freq:
        count = freq[word]
        items.append((word, count))
    items.sort(key=lambda i: (-i[1], i[0]))
    return items[:n]


a = ["a","b","a","c","b","a"]
b = ["bb","aa","bb","aa","cc"]
print(count_freq(a))
print(count_freq(b))
print(top_n(count_freq(a)))
print(top_n(count_freq(b)))