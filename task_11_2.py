"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class MyTypeError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f'{self.__class__.__name__}: {self.msg}'


a = input('Введите делимое: ')
b = input('Введите делитель: ')

# ВАРИАНТ 1
try:
    if int(b) == 0:
        raise MyTypeError('Делить на ноль нежелательно')
except MyTypeError as err:
    print(err)
else:
    print(f'Получилось: {int(a) / int(b)}')

# ВАРИАНТ 2
try:
    res = int(a) / int(b)
    print(f'Получилось: {res}')
except ZeroDivisionError:
    try:
        if int(b) == 0:
            raise MyTypeError('Делить на ноль нежелательно')
    except MyTypeError as err:
        print(err)
