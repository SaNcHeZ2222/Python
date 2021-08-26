dict_obj = {}


class ThereIsNoPlace(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    max_place = 6


class OfficeEquipment:
    min_place = 0
    class_name = ''
    def add_to_warehouse(self, name, count):
        Warehouse.max_place -= count
        try:
            if OfficeEquipment.min_place > Warehouse.max_place:
                raise ThereIsNoPlace('Нету больше места')
            else:
                if f'{self.class_name}' not in dict_obj.keys():
                    dict_obj[f'{self.class_name}'] = {'name': [name], 'count': [count]}
                else:
                    dict_obj[f'{self.class_name}']['name'].append(name)
                    dict_obj[f'{self.class_name}']['count'].append(count)
            print(dict_obj)
        except ThereIsNoPlace as err:
            print(err)


class Printer(OfficeEquipment):
    class_name = 'printer'

    def __init__(self, color='black'):
        self.color = color

    def add_to_warehouse_printer(self, name, count):
        self.add_to_warehouse(name=name, count=count)


class Copier(OfficeEquipment):
    class_name = 'copier'

    def __init__(self, color='green'):
        self.color = color

    def add_to_warehouse_printer(self, name, count):
        self.add_to_warehouse(name=name, count=count)


class Scanner(OfficeEquipment):
    class_name = 'scanner'

    def __init__(self, color='yellow'):
        self.color = color

    def add_to_warehouse_printer(self, name, count):
        self.add_to_warehouse(name=name, count=count)


one_printer = Printer()
one_printer.add_to_warehouse('Printer', 2)

one_printer.add_to_warehouse('Printer_1', 2)

one_scanner = Scanner()
one_scanner.add_to_warehouse('Scaner', 1)

one_copier = Copier()
one_copier.add_to_warehouse('Copier', 1)
