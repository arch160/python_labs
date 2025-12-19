from collections import deque
from typing import Any, Optional


class Stack:
    """
    Стек (LIFO) на базе списка Python.
    Вершина стека - последний элемент списка.
    """
    
    def __init__(self):
        """Инициализирует пустой стек."""
        self._data = []
    
    def push(self, item: Any) -> None:
        """
        Добавляет элемент на вершину стека.
        """
        self._data.append(item)
    
    def pop(self) -> Any:
        """
        Удаляет и возвращает элемент с вершины стека.
        
        Returns:
            Элемент с вершины стека.
        
        Raises:
            IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:
        """
        Возвращает элемент с вершины стека без удаления.
        
        Returns:
            Элемент с вершины стека или None, если стек пуст.
        """
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        
        Returns:
            True, если стек пуст, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке.
        
        Returns:
            Количество элементов.
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Stack({self._data})"


class Queue:
    """
    Очередь (FIFO) 
    """
    
    def __init__(self):
        """Инициализирует пустую очередь."""
        self._data = deque()
    
    def enqueue(self, item: Any) -> None:
        """
        Добавляет элемент в конец очереди.
        """
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """
        Удаляет и возвращает элемент из начала очереди.
        
        Returns:
            Элемент из начала очереди.
        
        Raises:
            IndexError: Если очередь пуста.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]:
        """
        Возвращает элемент из начала очереди без удаления.
        
        Returns:
            Элемент из начала очереди или None, если очередь пуста.
        """
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь.
        
        Returns:
            True, если очередь пуста, иначе False.
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди.
        
        Returns:
            Количество элементов.
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"
