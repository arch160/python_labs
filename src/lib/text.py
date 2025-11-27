"""
Модуль для работы с текстом
"""

from collections import Counter
import re
import sys
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    print(f"Читаю файл: {path}")
    p = Path(path)
    text = p.read_text(encoding=encoding)
    print(f"Прочитал {len(text)} символов")
    return text

def frequencies_from_text(text):
    """
    Анализирует текст и возвращает частоты слов
    
    Args:
        text (str): Входной текст
        
    Returns:
        dict: Словарь {слово: частота}
    """
    # Очищаем текст и разбиваем на слова
    words = text.lower().split()
    
    # Подсчитываем частоты
    return Counter(words)


def sorted_word_counts(freqs):
    """
    Сортирует слова по частоте (по убыванию)
    
    Args:
        freqs (dict): Словарь частот
        
    Returns:
        list: Список кортежей [(слово, частота), ...]
    """
    return sorted(freqs.items(), key=lambda x: x[1], reverse=True)

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    text = ' '.join(text.split())
    text = text.strip()
    return text

def tokenize(text: str) -> list[str]:
    t = r'[\w]+(?:-[\w]+)*'
    l = re.findall(t, text, re.UNICODE)
    return l


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