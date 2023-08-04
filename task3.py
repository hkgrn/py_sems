# Создайте класс Матрица. Добавьте методы для: вывода на печать, сравнения, сложения

class Matrix():
    """Init class matrix"""

    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        """EQ for 2 matrix"""

        if len(self.matrix) != len(other.matrix):
            return False
        else:
            flag = False
            for i in range(len(self.matrix)):
                if self.matrix[i] == other.matrix[i]:
                    flag = True
                else:
                    flag = False
            return flag

    def __add__(self, other):
        """Summ of 2 Matrix"""

        if len(self.matrix) != len(other.matrix):
            return "Сложение невозможно\n"
        else:
            result = []
            for i in range(len(self.matrix)):
                line_a = self.matrix[i]
                line_b = other.matrix[i]
                res = [x + y for x, y in zip(line_a, line_b)]
                result.append(res)
            return Matrix(result)

    def __str__(self):
        """Str for user"""

        result = "ИТОГОВАЯ МАТРИЦА: \n"
        for stroke in self.matrix:
            result += f'{stroke}\n'
        return result


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix([[1, 2, 3], [9, 5, 6]])
matrix_4 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]])

matrix_x = matrix_1 + matrix_2
matrix_y = matrix_1 + matrix_4
matrix_z = matrix_2 + matrix_3


print(matrix_x)
print(matrix_y)
print(matrix_z)

print(matrix_1 == matrix_2)
print(matrix_1 == matrix_4)
