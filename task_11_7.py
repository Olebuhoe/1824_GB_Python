"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные
числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class NoCompNumError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f'{self.__class__.__name__}: {self.msg}'


class ComplexNumbers:
    _imag_unit = 1j

    def __init__(self, a: float, b: float):
        self.real_part = a
        self.imag_part = b

    def __str__(self):
        return f'{self.real_part} + {self.imag_part}*{str(self._imag_unit)[1]}'

    def __add__(self, other):
        try:
            if not isinstance(other, ComplexNumbers):
                raise NoCompNumError('It is not a complex number!')
            else:
                return ComplexNumbers(self.real_part + other.real_part, self.imag_part + other.imag_part)
        except NoCompNumError as err:
            print(err)

    def __mul__(self, other):
        try:
            if not isinstance(other, ComplexNumbers):
                raise NoCompNumError('It is not a complex number!')
            else:
                return ComplexNumbers(self.real_part * other.real_part - self.imag_part * other.imag_part,
                                      self.real_part * other.real_part + self.imag_part * other.imag_part)
        except NoCompNumError as err:
            print(err)


x = ComplexNumbers(5, 3.5)
y = 6
print(x + y)
