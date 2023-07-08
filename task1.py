#  Напишите функцию для транспонирования матрицы
def transpose(matrix_: list[str]):
    return list(zip(*matrix_))


# matrix = [[1, -2, 3], [4, -5, 9]]
matrix = input('Введите строки матрицы через пробел (каждую строку - слитно, например: 123 456 789): ').split()
# Нужна подсказка, как добавить к выводу отрицательные значения

trans_matrix = transpose(matrix)
for i in range(len(trans_matrix)):
    print(trans_matrix[i])
