"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
(TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, name, color, is_police: bool):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self, speed):
        self.speed = speed
        print('Автомобиль движется')

    def stop(self):
        self.speed = 0
        print('Автомобиль не движется')

    def turn(self, direction):
        if self.speed > 0:
            if direction == 'right':
                print('Поворот направо')
            elif direction == 'left':
                print('Поворот налево')
            elif direction == 'reversal':
                print('Разворот')
            else:
                print('А это куда?')
        else:
            print('А мы походу никуда не едем, чувак...')

    def show_speed(self):
        print(f'Скорость автомобиля сейчас {self.speed} км/ч')


class TownCar(Car):
    max_travel_speed = 60

    def show_speed(self):
        if self.speed > self.max_travel_speed:
            print(f'Превышение скорости. Разрешенная скорость {self.max_travel_speed} км/ч, а у тебя {self.speed}')
        else:
            print(f'Скорость автомобиля сейчас {self.speed} км/ч')


class WorkCar(Car):
    max_travel_speed = 40

    def show_speed(self):
        if self.speed > self.max_travel_speed:
            print(f'Превышение скорости. Разрешенная скорость {self.max_travel_speed} км/ч, а у тебя {self.speed}')
        else:
            print(f'Скорость автомобиля сейчас {self.speed} км/ч')


class SportCar(Car):
    max_travel_speed = 400


class PoliceCar(Car):
    def __init__(self, name, color, is_police=True):
        super().__init__(name, color, is_police)


car_1 = TownCar('Audi', 'Blue', False)
car_1.go(50)
car_1.show_speed()
car_1.go(70)
car_1.show_speed()
car_1.turn('right')
car_1.turn('налево')
car_1.show_speed()
car_1.stop()
car_1.show_speed()
car_1.turn('left')
print(car_1.is_police)

car_2 = WorkCar('Dodge', 'Red', False)
car_2.go(50)
car_2.show_speed()
car_2.go(70)
car_2.show_speed()

car_3 = PoliceCar('Chevrolet', 'Blue-White')
print(car_3.color)
print(car_3.is_police)
