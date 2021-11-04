"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
 принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом
 сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем
 с первым элементом первой строки второй матрицы и пр.
"""


class Matrix:

    def __init__(self, list_of_list):
        for i in range(len(list_of_list) - 1):
            if len(list_of_list[i]) == len(list_of_list[i + 1]):
                self.list_of_list = list_of_list
            else:
                raise TypeError('This list is not suitable for forming a matrix')

    def __str__(self):
        return '\n'.join(['\t'.join([str(_) for _ in i]) for i in self.list_of_list])

    def __add__(self, other):
        if isinstance(other, Matrix) and\
                len(self.list_of_list) == len(other.list_of_list) and \
                len(self.list_of_list[0]) == len(other.list_of_list[0]):
            return Matrix([[x + y for x, y in zip(i, j)] for i, j in zip(self.list_of_list, other.list_of_list)])
        else:
            raise TypeError('One of arguments are not а Matrix or these are Matrix\'s of different sizes')


matrix1 = Matrix([[1, 22, 3], [4, 5, 6], [7, 8, 79]])
matrix2 = Matrix([[11, 2, 37, 1], [47, 15, 6, 2], [74, 81, 9, 3]])
print(matrix1)
print(matrix2)
print(matrix2 + matrix1)
