"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для
каждого типа оргтехники.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру (например, словарь).
Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
"""
from abc import abstractmethod


class OfficeEquipment:
    def __init__(self, tm: str, model: str, year: str):
        self.tm = tm
        self.model = model
        self.year = year

    @abstractmethod
    def functional(self):
        print('Это оргтехника. Она помогает в офисе.')


class Printer(OfficeEquipment):
    def __init__(self, tm, model, year, serial):
        super().__init__(tm, model, year)
        self.serial = serial
        self.name = self.__class__.__name__

    def __str__(self):
        return f'{self.tm} {self.model}, {self.year} г.в., s/n {self.serial}, {self.name}'

    def functional(self):
        print('Это принтер. Он печатает.')


class Scanner(OfficeEquipment):
    def __init__(self, tm, model, year, serial):
        super().__init__(tm, model, year)
        self.serial = serial

    def __str__(self):
        return f'{self.tm} {self.model}, {self.year} г.в., s/n {self.serial}, {self.__class__.__name__}'

    def functional(self):
        print('Это сканер. Он сканирует.')


class Xerox(OfficeEquipment):
    def __init__(self, tm, model, year, serial):
        super().__init__(tm, model, year)
        self.serial = serial

    def __str__(self):
        return f'{self.tm} {self.model}, {self.year} г.в., s/n {self.serial}, {self.__class__.__name__}'

    def functional(self):
        print('Это ксерокс. Он копирует.')


class Warehouse:
    def __init__(self):
        self.p_storage: set = set()
        self.s_storage: set = set()
        self.x_storage: set = set()

    def __str__(self):
        return f'{self.p_storage}, {self.s_storage}, {self.x_storage}'

    def invent(self):
        """Метод инвентаризации складских остатков"""
        print(f'Всего на складе {len(self.p_storage) + len(self.s_storage) + len(self.x_storage)} ед. офисной '
              f'техники.\nИз них: {len(self.p_storage)} принтеров, {len(self.s_storage)} сканеров, '
              f'{len(self.x_storage)} ксероксов. А именно:')
        for _ in self.p_storage:
            print(_)
        for _ in self.x_storage:
            print(_)
        for _ in self.s_storage:
            print(_)

    # def __del__(self):
    #     print(f'Склад {self} аннулирован')

    def arrival(self, *equipments):
        """Метод приемки оргтехники на склад"""
        for equipment in equipments:
            if isinstance(equipment, Printer):
                self.p_storage.add(equipment)
            elif isinstance(equipment, Scanner):
                self.s_storage.add(equipment)
            else:
                self.x_storage.add(equipment)

    def consumption(self, destination, *equipments):
        """Метод списания оргтехники со склада в соответствующее подразделение Офиса
        по наименованиям конкретных единиц оргтехники"""
        for equipment in equipments:
            if isinstance(equipment, Printer):
                destination.storage.add(self.p_storage.pop())
            elif isinstance(equipment, Scanner):
                destination.storage.add(self.s_storage.pop())
            else:
                destination.storage.add(self.x_storage.pop())

    def consumption_in_pieces(self, destination, kind_equip, amount):
        """(для 6 задания) Метод списания оргтехники со склада в соответствующее подразделение Офиса
        по необходимому количеству конкретного вида оргтехники"""
        if not str(amount).isdigit():
            raise ValueError(f'Нельзя переместить "{amount}" ед. оргтехники')
        elif kind_equip.lower() == 'printer' and amount > len(self.p_storage):
            raise ValueError('На складе нет столько принтеров')
        elif kind_equip.lower() == 'scanner' and amount > len(self.s_storage):
            raise ValueError('На складе нет столько сканеров')
        elif kind_equip.lower() == 'xerox' and amount > len(self.x_storage):
            raise ValueError('На складе нет столько ксероксов')
        else:
            if kind_equip.lower() == 'printer':
                for _ in range(amount):
                    destination.storage.add(self.p_storage.pop())
            elif kind_equip.lower() == 'scanner':
                for _ in range(amount):
                    destination.storage.add(self.s_storage.pop())
            else:
                for _ in range(amount):
                    destination.storage.add(self.x_storage.pop())


class Office:
    def __init__(self, name: str):
        self.storage: set = set()
        self.name = name

    def invent(self):
        """Метод инвентаризации техники в подразделениях Офиса"""
        print(f'Всего в подразделении {self.name} {len(self.storage)} ед. офисной техники:')
        for _ in self.storage:
            print(_)


p_1 = Printer('Canon', 'LBP6020', '2015', '123456')
x_1 = Xerox('Xerox', 'X546', '2010', '654852')
p_2 = Printer('HP', 'PH4556', '2014', '785264')
sales_dep = Office('Отдел продаж')
storage = Warehouse()
storage.arrival(p_1, x_1, p_2)
storage.invent()
print('==========END=========')
# storage.consumption(sales_dep, p_1, x_1)
# storage.invent()
# print('==========END=========')
# sales_dep.invent()
# print('==========END=========')
# bookkeeping = Office('Бухгалтерия')
# storage.consumption(bookkeeping, p_2)
# storage.invent()
# print('==========END=========')
# bookkeeping.invent()

storage.consumption_in_pieces(sales_dep, 'xerox', 2)
sales_dep.invent()
print('==========END=========')
storage.invent()
