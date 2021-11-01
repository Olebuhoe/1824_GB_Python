"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print('Для письма')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print('Для черчения')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print('Для рисования')


chalk = Stationery()
chalk.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
