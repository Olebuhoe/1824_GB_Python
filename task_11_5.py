"""
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру (например, словарь).
"""


class Warehouse:
    def __init__(self):
        self.warehouse = {}
        # self.gross_buh: dict = {}

    def arrival(self, equipment):
        self.warehouse.setdefault(self.__class__.__name__, []).append(equipment)

    def extract(self):
        if self.warehouse[name]:
            self.warehouse.setdefault(name).pop(0)