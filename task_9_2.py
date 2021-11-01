"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной
в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _asphalt_density = 18

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_consumption(self, pavement_thickness):
        asph_weight = self._length * self._width * self._asphalt_density * pavement_thickness / 1000
        return asph_weight


road = Road(100.5, 10)
print(road.asphalt_consumption(10))
