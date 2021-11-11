class NoCompNumError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f'{self.__class__.__name__}: {self.msg}'


def valid_obj(other, cls, err, msg: str):
    """Функция для валидации объекта класса и возбуждения ошибки"""
    if not isinstance(other, cls):
        raise err(msg)


class ComplexNumbers:
    _imag_unit = 1j

    def __init__(self, a: float, b: float):
        self.real_part = a
        self.imag_part = b

    def __str__(self):
        return f'{self.real_part} + {self.imag_part}*{str(self._imag_unit)[1]}'

    def __add__(self, other):
        try:
            if valid_obj(other, ComplexNumbers, NoCompNumError, 'It is not a complex number!'):
                pass
            else:
                return ComplexNumbers(self.real_part + other.real_part, self.imag_part + other.imag_part)
        except NoCompNumError as err:
            print(err)

    def __mul__(self, other):
        try:
            if valid_obj(other, ComplexNumbers, NoCompNumError, 'It is not a complex number!'):
                pass
            else:
                return ComplexNumbers(self.real_part * other.real_part - self.imag_part * other.imag_part,
                                      self.real_part * other.real_part + self.imag_part * other.imag_part)
        except NoCompNumError as err:
            print(err)


x = ComplexNumbers(5, 3.5)
# y = ComplexNumbers(6.3, -2)
y = 9
print(x * y)
