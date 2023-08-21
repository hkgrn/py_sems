import os
from collections import namedtuple
import logging
import sys

# Настройка
logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Определение namedtuple
FileInfo = namedtuple('FileInfo', ['name_without_extension', 'extension', 'is_directory', 'parent_directory'])


def gather_file_info(directory_path):
    # Проверяем существование
    if not os.path.exists(directory_path):
        logging.error(f"Директория {directory_path} не существует.")
        return

    # Поиск
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(item_path)
        name, extension = os.path.splitext(item)

        # Создаем объект FileInfo и записываем информацию в лог
        file_info = FileInfo(name, extension, is_directory, os.path.basename(directory_path))
        logging.info(file_info)


if __name__ == "__main__":
    # Система
    if len(sys.argv) != 2:
        print("Использование: python task1.py <путь>")
        sys.exit(1)

    directory_path = sys.argv[1]
    gather_file_info(directory_path)