from typing import Any, Iterator, Optional


class Node:
    """
    Узел односвязного списка.
    
    Attributes:
        value: Значение элемента.
        next: Ссылка на следующий узел.
    """
    
    def __init__(self, value: Any, next: Optional['Node'] = None):
        """
        Инициализирует узел.
        
        Args:
            value: Значение узла.
            next: Ссылка на следующий узел.
        """
        self.value = value
        self.next = next
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    Односвязный список.
    
    Attributes:
        head: Первый узел списка.
        tail: Последний узел списка.
        _size: Количество элементов.
    """
    
    def __init__(self):
        """Инициализирует пустой список."""
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, value: Any) -> None:
        """
        Добавляет элемент в конец списка.
        
        Args:
            value: Значение для добавления.
        """
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """
        Добавляет элемент в начало списка.
        
        Args:
            value: Значение для добавления.
        """
        new_node = Node(value, self.head)
        self.head = new_node
        
        if self.tail is None:
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """
        Вставляет элемент по указанному индексу.
        
        Args:
            idx: Индекс для вставки (от 0 до len(list)).
            value: Значение для вставки.
        
        Raises:
            IndexError: Если индекс вне диапазона.
        """
        if idx < 0 or idx > self._size:
            raise IndexError(f"index {idx} out of range [0, {self._size}]")
        
        # Вставка в начало
        if idx == 0:
            self.prepend(value)
            return
        
        # Вставка в конец
        if idx == self._size:
            self.append(value)
            return
        
        # Вставка в середину
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1
    
    def remove(self, value: Any) -> None:
        """
        Удаляет первое вхождение указанного значения.
        """
        # Пустой список
        if self.head is None:
            return
        
        # Удаление из начала
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            
            if self.head is None:  # Список стал пустым
                self.tail = None
            return
        
        # Поиск узла для удаления
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        # Значение не найдено
        if current.next is None:
            return
        
        # Удаление узла
        current.next = current.next.next
        self._size -= 1
        
        # Если удалили последний элемент
        if current.next is None:
            self.tail = current
    
    def remove_at(self, idx: int) -> Any:
        """
        Удаляет элемент по указанному индексу.
        
        Returns:
            Значение удаленного элемента.
        
        Raises:
            IndexError: Если индекс вне диапазона.
        """
        if idx < 0 or idx >= self._size:
            raise IndexError(f"index {idx} out of range [0, {self._size - 1}]")
        
        # Удаление из начала
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            self._size -= 1
            
            if self.head is None:  # Список стал пустым
                self.tail = None
            
            return value
        
        # Поиск узла перед удаляемым
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        # Удаление узла
        value = current.next.value
        current.next = current.next.next
        self._size -= 1
        
        # Если удалили последний элемент
        if current.next is None:
            self.tail = current
        
        return value
    
    def __iter__(self) -> Iterator[Any]:
        """
        Возвращает итератор по значениям списка.
        
        Yields:
            Значения элементов в порядке от начала к концу.
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в списке.
        
        Returns:
            Количество элементов.
        """
        return self._size
    
    def __repr__(self) -> str:
        values = list(self)
        return f"SinglyLinkedList({values})"

