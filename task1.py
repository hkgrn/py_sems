# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = input("Введите элементы списка через пробел: ").split()
lst_double = []

for i in range(len(lst)):
    if lst.count(lst[i]) > 1 and lst[i] not in lst_double:
        lst_double.append(lst[i])

print('Список дублирующихся элементов: ', lst_double)



