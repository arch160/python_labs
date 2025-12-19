# Лабораторная работа № 10

## Теория

### Стек (Stack)
*Стек — структура данных, работающая по принципу LIFO (Last In, First Out — "последним пришел, первым ушел").

*Основные операции и их сложность:
- `push(item)` — добавление элемента на вершину стека: O(1)
- `pop()` — удаление и возврат элемента с вершины: O(1)
- `peek()` — просмотр элемента на вершине без удаления: O(1)
- `is_empty()` — проверка на пустоту: O(1)

### Очередь (Queue)
*Очередь — структура данных, работающая по принципу FIFO (First In, First Out — "первым пришел, первым ушел").

Основные операции и их сложность:
- `enqueue(item)` — добавление элемента в конец очереди: O(1)
- `dequeue()` — удаление и возврат элемента из начала: O(1)
- `peek()` — просмотр первого элемента без удаления: O(1)
- `is_empty()` — проверка на пустоту: O(1)

### Односвязный список (Singly Linked List)
*Связный список — динамическая структура данных, состоящая из узлов, каждый из которых содержит значение и ссылку на следующий узел.

Основные операции и их сложность:
- `append(value)` — добавление в конец: O(1) с tail, O(n) без tail
- `prepend(value)` — добавление в начало: O(1)
- `insert(idx, value)` — вставка по индексу: O(n) в худшем случае
- `remove(value)` — удаление по значению: O(n)
- `remove_at(idx)` — удаление по индексу: O(n)
- Поиск элемента: O(n)
- Доступ по индексу: O(n)

## Structures
```python
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
```

## Linked_list

```python
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
```

## Тестируем:

### Stack
```python
from src.lab10.structures import Stack
s = Stack()
s.push(1)
s.push(2)    
print(s.peek())
print(s.pop())  
print(s.pop())  
print(s.is_empty()) 
```

![101](../../images/lab10/101.png)

### Queue
```python 
from src.lab10.structures import Queue
q = Queue()
q.enqueue('A')
q.enqueue('B')    
q.enqueue('C')    
print(q.peek())    
print(q.dequeue()) 
print(q.dequeue()) 
print(len(q))
```
![102](../../images/lab10/102.png)


### SinglyLinkedList
```python
from src.lab10.linked_list import SinglyLinkedList
lst = SinglyLinkedList()
lst.append(10)     
lst.prepend(5)    
lst.append(20)      
lst.insert(2, 15)   

for value in lst:
    print(value)    


lst.remove(10)     
print(lst.remove_at(1))  

print(len(lst))    
print(lst)         
```

![103](../../images/lab10/103.png)