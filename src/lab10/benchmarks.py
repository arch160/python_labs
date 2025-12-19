import time
from structures import Stack, Queue
from linked_list import SinglyLinkedList

def benchmark_comprehensive():
    n = 10000
    
    print("=" * 40)
    print(f"БЕНЧМАРК {n} ОПЕРАЦИЙ")
    print("=" * 40)
    
    # 1. ТЕСТ ДОСТУПА ПО ИНДЕКСУ (чтение)
    print("\n1. ДОСТУП ПО ИНДЕКСУ (чтение):")
    
    # Подготовка данных
    ll = SinglyLinkedList()
    py_list = []
    for i in range(n):
        ll.append(i)
        py_list.append(i)
    
    # Тест вашего списка (медленно - O(n))
    start = time.time()
    for i in range(1000):  # меньше операций, так как медленно
        # Имитируем доступ - идем от начала
        current = ll.head
        for _ in range(i % 100):
            if current:
                current = current.next
    print(f"  SinglyLinkedList: {(time.time()-start):.3f} сек (медленно)")
    
    # Тест встроенного list (быстро - O(1))
    start = time.time()
    for i in range(n):
        _ = py_list[i % n]  # Быстрый доступ
    print(f"  Встроенный list:  {(time.time()-start):.3f} сек (быстро)")
    
    # 2. ТЕСТ ПОИСКА ЭЛЕМЕНТА
    print("\n2. ПОИСК ЭЛЕМЕНТА (значение в конце):")
    
    # Ваш список
    start = time.time()
    for i in range(100):
        current = ll.head
        while current and current.value != n-1:
            current = current.next
    print(f"  SinglyLinkedList: {(time.time()-start):.3f} сек (O(n))")
    
    # Встроенный list
    start = time.time()
    for i in range(100):
        _ = n-1 in py_list  # Поиск по значению
    print(f"  Встроенный list:  {(time.time()-start):.3f} сек (O(n))")
    
    # 3. ТЕСТ УДАЛЕНИЯ ИЗ НАЧАЛА
    print("\n3. УДАЛЕНИЕ ИЗ НАЧАЛА:")
    
    # Ваш список
    ll2 = SinglyLinkedList()
    for i in range(n): ll2.append(i)
    start = time.time()
    for i in range(1000):
        if ll2.head:
            ll2.remove_at(0)  # O(1)
    print(f"  SinglyLinkedList remove_at(0): {(time.time()-start):.3f} сек")
    
    # Встроенный list
    py_list2 = list(range(n))
    start = time.time()
    for i in range(1000):
        if py_list2:
            py_list2.pop(0)  # O(n) - медленно!
    print(f"  Встроенный list pop(0):        {(time.time()-start):.3f} сек")
    
    # 4. ТЕСТ УДАЛЕНИЯ ИЗ КОНЦА
    print("\n4. УДАЛЕНИЕ ИЗ КОНЦА:")
    
    # Ваш список
    ll3 = SinglyLinkedList()
    for i in range(n): ll3.append(i)
    start = time.time()
    for i in range(1000):
        if len(ll3) > 0:
            ll3.remove_at(len(ll3)-1)  # O(n) без tail->prev!
    print(f"  SinglyLinkedList remove_at(-1): {(time.time()-start):.3f} сек (медленно)")
    
    # Встроенный list
    py_list3 = list(range(n))
    start = time.time()
    for i in range(1000):
        if py_list3:
            py_list3.pop()  # O(1) - быстро!
    print(f"  Встроенный list pop():         {(time.time()-start):.3f} сек (быстро)")
    
    # 5. ТЕСТ ПАМЯТИ (косвенный)
    print("\n5. ИСПОЛЬЗОВАНИЕ ПАМЯТИ:")
    import sys
    
    ll_test = SinglyLinkedList()
    for i in range(1000): ll_test.append(i)
    
    py_test = list(range(1000))
    
    # Оцениваем размер (примерно)
    ll_size = sys.getsizeof(ll_test) + 1000 * sys.getsizeof(ll_test.head)
    py_size = sys.getsizeof(py_test) + 1000 * sys.getsizeof(py_test[0])
    
    print(f"  SinglyLinkedList: ~{ll_size//1000}КБ (больше - хранит ссылки)")
    print(f"  Встроенный list:  ~{py_size//1000}КБ (компактнее)")

if __name__ == "__main__":
    benchmark_comprehensive()