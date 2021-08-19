class Worker:
    def __init__(self, n, s, p, i):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {'wage': int(i.split()[0]), "bonus": int(i.split()[1])}

    def get_income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(sum(self.get_income().values()))


a = Position("Александр", "Байбаков", "Python-разработчик", '50000 5000')
a.get_full_name()
a.get_total_income()
print(a.get_income())