"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import re


class Date:
    @staticmethod
    def date_validate(date: str):
        days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        lst = [*map(int, date.split('-'))]
        sample = re.compile(r'^(\d{2}-){2}\d{4}$')
        if not sample.match(date):
            raise ValueError('Дата должна быть в формате "ДД-ММ-ГГГГ"')
        elif lst[1] > len(days_in_months):
            raise ValueError('Проверьте номер месяца, в году их всего 12')
        elif lst[0] > days_in_months[lst[1] - 1] and sample.match(date):
            raise ValueError('Проверьте количество дней в месяце')
        else:
            return True

    def __init__(self, date: str):
        if self.date_validate(date):
            self.date = date

    @classmethod
    def extract(cls, date: str):
        if cls.date_validate(date):
            return map(int, date.split('-'))


d = Date('31-01-1980')
print(*Date.extract('03-10-1980'))
print(Date.date_validate('30-12-1980'))
