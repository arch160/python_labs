"""
Модуль для работы с текстом
"""

from collections import Counter


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