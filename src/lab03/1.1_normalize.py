def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text = text.casefold()
    text = " ".join(text.split())
    text = text.strip()
    return text


a = "ПрИвЕт\nМИр\t"
b = "ёжик, Ёлка"
c = "Hello\r\nWorld"
d = "  двойные   пробелы  "
print(normalize(a))
print(normalize(b))
print(normalize(c))
print(normalize(d))
