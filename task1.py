import os

def group_file_rename(desired_name, num_digits, source_extension, target_extension, name_range):
    directory = os.getcwd()
    counter = 0

    for filename in os.listdir(directory):
        if filename.endswith(source_extension):
            original_name = filename[:-len(source_extension)]  # Имя файла без расширения
            # Обрезаем имя файла в соответствии с указанным диапазоном
            trimmed_name = original_name[name_range[0]-1:name_range[1]-1]

            # Создаем новое имя файла
            new_name = trimmed_name + '_' + desired_name + str(counter).zfill(num_digits) + '.' + target_extension
            # Полный путь к исходному и конечному файлу
            source_path = os.path.join(directory, filename)
            target_path = os.path.join(directory, new_name)

            # Переименовываем файл
            os.rename(source_path, target_path)

            counter += 1

# Вызов (пример)
group_file_rename('rename', 3, '.md', 'txt', [3, 6])