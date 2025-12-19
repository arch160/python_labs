from pathlib import Path
import sys

current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from io_txt_csv import normalize, tokenize, count_freq, top_n, read_text, write_csv


def main():
    current_file = Path(__file__)
    print(f"Текущий файл: {current_file}")
    
    # Проверка существования текущего файла
    if not current_file.exists():
        print(f"ОШИБКА: Файл {current_file} не существует")
        return
    
    input_path = current_file.parent / "data" / "input.txt"
    output_path = current_file.parent / "data" / "output.csv"
    
    print(f"Путь к входному файлу: {input_path}")
    print(f"Путь к выходному файлу: {output_path}")
    
    # Проверка и создание директории data
    data_dir = input_path.parent
    if not data_dir.exists():
        print(f"Создание директории: {data_dir}")
        try:
            data_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"ОШИБКА: Не удалось создать директорию {data_dir}: {e}")
            return
    
    # Проверка создания/записи входного файла
    try:
        input_path.write_text("Привет, мир! Привет!!!", encoding="utf-8")
        print(f"Создан/обновлен файл: {input_path}")
    except Exception as e:
        print(f"ОШИБКА: Не удалось записать в файл {input_path}: {e}")
        return
    
    # Проверка существования входного файла
    if not input_path.exists():
        print(f"ОШИБКА: Входной файл {input_path} не создан")
        return
    
    # Проверка размера входного файла
    file_size = input_path.stat().st_size
    if file_size == 0:
        print(f"ПРЕДУПРЕЖДЕНИЕ: Входной файл пуст")
    
    result = read_text(input_path)
    print(f"Результат чтения: {result}")
    
    normalized_text = normalize(result)
    print(f"Нормализованный текст: {normalized_text}")
    
    tokens = tokenize(normalized_text)
    print(f"Токены: {tokens}")
    
    frequencies = count_freq(tokens)
    print(f"Частоты: {frequencies}")
    
    word_counts = top_n(frequencies, n=len(frequencies))
    print(f"Подсчет слов: {word_counts}")
    
    # Проверка возможности записи в выходной файл
    try:
        write_csv(word_counts, output_path, header=("word", "count"))
        print(f"CSV файл создан: {output_path}")
        
        # Проверка существования выходного файла
        if output_path.exists():
            output_size = output_path.stat().st_size
            print(f"Размер выходного файла: {output_size} байт")
        else:
            print(f"ПРЕДУПРЕЖДЕНИЕ: Выходной файл не создан")
    except Exception as e:
        print(f"ОШИБКА: Не удалось записать CSV файл {output_path}: {e}")


if __name__ == "__main__":
    main()