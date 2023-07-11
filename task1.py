# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def path_tuple(inp: str) -> tuple:
    # Разбиваем абсолютный путь на расположение, наименование и расширение.
    *link_parts, file_full = inp.split('\\')
    file, extension = file_full.split('.')
    link = '\\'.join(link_parts)
    # Возвращаем кортеж из значений переменных.
    return link, file, extension


path = input('Введите путь до файла: ')
# Пример: C:\Program Files (x86)\EasyAntiCheat_EOS\test.txt
print(path_tuple(path))
