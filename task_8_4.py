from functools import wraps


def val_checker(f):  # работает до первого невалидного аргумента, его же и включает в ошибку
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for arg in args:
                if f(arg):
                    continue
                else:
                    raise ValueError(f'wrong val: {arg}')
            for k, v in kwargs.items():
                if f(v):
                    continue
                else:
                    raise ValueError(f'wrong val: {v}')
            return result
        return wrapper
    return _val_checker


# @val_checker(lambda x: x > 0)
# def sum_num(*x):
#     return sum(x)
#
#
# print(sum_num(2, 3, -4))


@val_checker(lambda x: x > 0)
def kek(x, y, z):
    return x * y * z


print(kek(4, 2.5, z=-5))


# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# print(calc_cube(-3))
