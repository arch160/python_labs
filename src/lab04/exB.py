from pathlib import Path
from io_txt_csv import normalize, tokenize, count_freq, top_n, read_text, write_csv

current_file = Path(__file__)

# Проверка существования текущего файла
if not current_file.exists():
    print(f"ОШИБКА: Файл {current_file} не существует")
    exit(1)

input_path = current_file.parent.parent / "src/data/input_test.txt"
output_path = current_file.parent.parent / "src/data/output.csv"

print(f"Текущий файл: {current_file}")
print(f"Входной файл: {input_path}")
print(f"Выходной файл: {output_path}")

# Проверка и создание директории src/data
input_dir = input_path.parent
if not input_dir.exists():
    print(f"Создание директории: {input_dir}")
    try:
        input_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"ОШИБКА: Не удалось создать директорию {input_dir}: {e}")
        exit(1)

# Проверка входного файла
if input_path.exists():
    print(f"Удаление существующего файла: {input_path}")
    try:
        input_path.unlink()
    except Exception as e:
        print(f"ОШИБКА: Не удалось удалить файл {input_path}: {e}")
        exit(1)

# Проверка создания входного файла
try:
    input_path.write_text("Привет", encoding="utf-8")
    print(f"Создан пустой файл: {input_path}")
    
    # Проверка размера файла
    file_size = input_path.stat().st_size
    print(f"Размер входного файла: {file_size} байт")
except Exception as e:
    print(f"ОШИБКА: Не удалось создать файл {input_path}: {e}")
    exit(1)

text = read_text(input_path, "utf-8")
print(f"Прочитано: '{text}' ({len(text)} символов)")

normalized_text = normalize(text)
tokens = tokenize(normalized_text)
frequencies = count_freq(tokens)

print(f"Токены: {tokens}")
print(f"Частоты: {frequencies}")

word_counts = top_n(frequencies, n=len(frequencies))

# Проверка создания выходного файла
try:
    write_csv(
        [[word, count] for word, count in word_counts],
        output_path,
        header=("word", "count"),
    )
    print(f"CSV создан: {output_path}")
    
    # Проверка существования выходного файла
    if output_path.exists():
        output_size = output_path.stat().st_size
        print(f"Размер выходного файла: {output_size} байт")
    else:
        print(f"ПРЕДУПРЕЖДЕНИЕ: Выходной файл не создан")
except Exception as e:
    print(f"ОШИБКА: Не удалось создать CSV файл {output_path}: {e}")
    exit(1)

print(f"Всего слов: {sum(frequencies.values())}")
print(f"Уникальных слов: {len(frequencies)}")

print("Топ 5 слов:")
top_5 = top_n(frequencies, n=5)
for i, (word, count) in enumerate(top_5, 1):
    print(f"  {i}. '{word}': {count}") if top_5 else print("  Нет слов")
