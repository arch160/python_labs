import pytest
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '..', 'src')
sys.path.insert(0, src_path)

from lib.text import normalize, tokenize, count_freq, top_n

@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),  
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"), 
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected

@pytest.mark.parametrize(
    "source, expected",
    [
        ("Привет, друзья!", ["Привет", "друзья"]),
        ("Python programming", ["Python", "programming"]),
        (" ", []),
        ("###$$$%%%", []),
        ("e-mail пользователя", ["e-mail", "пользователя"]),
        ("42 3.14 100", ["42", "3", "14", "100"]), 
        ("apple banana apple", ["apple", "banana", "apple"]),
        ("один два три", ["один", "два", "три"]),
        ("C++ Java Python", ["C", "Java", "Python"]),  
        ("   multiple   spaces   ", ["multiple", "spaces"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected

@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["привет", "мир", "привет"], {"привет": 2, "мир": 1}),
        (["Python", "programming"], {"Python": 1, "programming": 1}),
        ([], {}),
        (["###$$$%%%"], {"###$$$%%%": 1}),
        (["e-mail", "пользователя"], {"e-mail": 1, "пользователя": 1}),
        (["42", "3", "14", "100"], {"42": 1, "3": 1, "14": 1, "100": 1}), 
        (["apple", "banana", "apple"], {"apple": 2, "banana": 1}),
        (["один", "два", "три"], {"один": 1, "два": 1, "три": 1}),
        (["C", "Java", "Python"], {"C": 1, "Java": 1, "Python": 1}), 
    ],
)
def test_count_freq_basic(tokens, expected):
    assert count_freq(tokens) == expected
    
@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"привет": 2, "мир": 1}, 2, [("привет", 2), ("мир", 1)]),
        ({"Python": 1, "programming": 1}, 1, [("Python", 1)]),
        ({}, 5, []),
        ({"###$$$%%%": 1}, 5, [("###$$$%%%", 1)]),
        ({"e-mail": 1, "пользователя": 1}, 2, [("e-mail", 1), ("пользователя", 1)]),
        ({"42": 1, "3.14": 1, "100": 1}, 3, [("100", 1), ("3.14", 1), ("42", 1)]),
    ],
)
def test_top_n_basic(freq, n, expected):
    assert top_n(freq, n) == expected

def test_top_n_tie_breaker():
    """Тест для случая с одинаковой частотой - должна быть сортировка по алфавиту"""
    freq = {"яблоко": 2, "банан": 2, "апельсин": 2, "вишня": 1}
    result = top_n(freq, 3)
    expected = [("апельсин", 2), ("банан", 2), ("яблоко", 2)]
    assert result == expected