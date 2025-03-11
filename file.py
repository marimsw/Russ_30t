# Перенос файлов из папки и excel файла в определенную директорию
import pandas as pd
import shutil
import os

# Параметры
excel_file_path = '28.02 Кредит_Ипотека30t.xlsx'  # Укажите путь к вашему Excel файлу
source_folder = 'C:/Загрузки/30 тысяч/russ2024y_cleaned'  # Укажите путь к папке-источнику с изображениями
destination_folder = 'C:/Загрузки/30 тысяч/Кредит_ипотека'  # Укажите путь к папке назначения

# Чтение Excel файла
df = pd.read_excel(excel_file_path)

# имена изображений находятся в первом столбце
image_filenames = df.iloc[:, 0].tolist()

# Копирование изображений
for filename in image_filenames:
    source_file = os.path.join(source_folder, filename)
    destination_file = os.path.join(destination_folder, filename)

    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
        print(f'Копирование: {source_file} в {destination_file}')
    else:
        print(f'Файл не найден: {source_file}')
