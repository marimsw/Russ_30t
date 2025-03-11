# Извлекает определенную категорию(который задал пользователь) из общего документа excel и создает новый excel файл,для дальнейшей работы

import pandas as pd

def extract_category_files_with_category_and_encoding_excel(input_csv_path: str, category_to_find: str, output_excel_path: str, separator: str = ','):
    """
    Извлекает значения file_name из CSV-файла, соответствующие заданной категории,
    и выводит вместе с категорией (которую искали). Сохраняет результат в Excel-файл.
    Добавлена поддержка кодировки, разделителя и сохранения в Excel.
    Обрабатывает случаи, когда в строке несколько категорий, разделенных разделителем.

    Args:
        input_csv_path: Путь к входному CSV-файлу.
        category_to_find: Категория для поиска (ввод с клавиатуры).
        output_excel_path: Путь к выходному Excel-файлу.
        separator: Разделитель между категориями в столбце 'category' (по умолчанию ',').
    """
    try:
        # Чтение CSV-файла с помощью pandas
        df = pd.read_csv(input_csv_path, encoding='utf-8')  # Кодировку можно указать здесь

        # Проверка наличия необходимых столбцов
        if 'category' not in df.columns or 'file_name' not in df.columns:
            print("Ошибка: CSV файл должен содержать столбцы 'category' и 'file_name'.")
            return

        # Фильтрация данных по заданной категории, учитывая несколько категорий в одной ячейке
        filtered_rows = []
        for index, row in df.iterrows():
            categories = str(row['category']).split(separator)  # Разделяем категории по разделителю, преобразуем в строку на случай NaN
            if category_to_find in [cat.strip() for cat in categories]: # убираем пробелы в начале и конце
                filtered_rows.append(row)

        filtered_df = pd.DataFrame(filtered_rows)

        # Выбор столбца file_name и добавление столбца category
        # Создаем новый DataFrame с file_name и category
        result_df = filtered_df[['file_name', 'category']]


        # Сохранение результатов в Excel файл
        result_df.to_excel(output_excel_path, index=False)  # Убрали encoding
        print(f"Файл успешно создан: {output_excel_path}")


    except FileNotFoundError:
        print(f"Ошибка: Файл не найден: {input_csv_path}")
    except UnicodeDecodeError:
        print(f"Ошибка: Не удалось декодировать файл. Попробуйте другую кодировку (например, 'cp1251', 'latin-1').")
    except Exception as e:
        print(f"Произошла ошибка при обработке CSV файла: {e}")


# Пример использования:
#input_csv = input("Введите путь к вашему CSV файлу: ")
input_csv = 'labels_russ2024y.csv'
category = input("Введите категорию для поиска: ")
output_excel = input('Путь к выходному Excel-файлу')  # Имя для нового Excel файла  (изменил расширение)

# Запрос разделителя у пользователя
separator = input("Введите разделитель для категорий (по умолчанию ','): ")
if not separator:
    separator = ','


extract_category_files_with_category_and_encoding_excel(input_csv, category, output_excel, separator)
