import re

def tokenize(text: str) -> list[str]:
    t = r'[\w]+(?:-[\w]+)*'
    l = re.findall(t, text, re.UNICODE)
    return l

a = "привет мир"
b = "hello,world!!!"
c = "по-настоящему круто"
d = "2025 год"
e = "emoji 😀 не слово"
print(tokenize(a))
print(tokenize(b))
print(tokenize(c))
print(tokenize(d))
print(tokenize(e))