class Warehouse:
    def __init__(self):
        self.p_storage: set = set()
        self.s_storage: set = set()
        self.x_storage: set = set()

    def __str__(self):
        return f'{self.p_storage}, {self.s_storage}, {self.x_storage}'

    def invent(self):
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
        for equipment in equipments:
            if isinstance(equipment, Printer):
                self.p_storage.add(equipment)
            elif isinstance(equipment, Scanner):
                self.s_storage.add(equipment)
            else:
                self.x_storage.add(equipment)

    def consumption(self, destination, *equipments):
        for equipment in equipments:
            if isinstance(equipment, Printer):
                destination.storage.add(self.p_storage.pop())
            elif isinstance(equipment, Scanner):
                destination.storage.add(self.s_storage.pop())
            else:
                destination.storage.add(self.x_storage.pop())

    def consumption_in_pieces(self, destination, kind_equip, amount):
        if amount > len(self.p_storage):
            raise ValueError('На складе нет столько техники')
        elif not str(amount).isdigit():
            raise ValueError(f'Нельзя переместить {amount} ед. оргтехники')
        else:
            if isinstance(kind_equip, Printer):
                for _ in range(amount):
                    destination.storage.add(self.p_storage.pop())
            elif isinstance(kind_equip, Scanner):
                for _ in range(amount):
                    destination.storage.add(self.s_storage.pop())
            else:
                for _ in range(amount):
                    destination.storage.add(self.x_storage.pop())


