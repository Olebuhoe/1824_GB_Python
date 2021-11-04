"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def cloth_calc(self):
        pass

    def __add__(self, other):
        return f'Общий расход ткани составит {self.cloth_calc + other.cloth_calc:.2f}'


class Coat(Clothes):
    def __init__(self, width):
        self.width = width

    @property
    def cloth_calc(self):
        return round(self.width / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def cloth_calc(self):
        return round(2 * self.height + 0.3, 2)


coat = Coat(50.0)
suit = Costume(2)
print(coat.cloth_calc)
print(suit.cloth_calc)
print(suit + coat)
