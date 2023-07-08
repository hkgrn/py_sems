# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.

def vocabulary(**kwargs):
    final_voc = {}
    for key, value in kwargs.items():
        final_voc[str(value)] = key
    return final_voc


print(vocabulary(one=1, two=2, three='3', four=4.44, five=[4, 5, 8]))
