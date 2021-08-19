class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print('Запуск зарисовки', end=' ')


class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('ручкой', end=' ')
        print()


class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('карандашом', end=' ')
        print()


class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print('маркером', end=' ')
        print()


a = Pen('Рисунок_1')
a.draw()

b = Pencil('Рисунок_2')
b.draw()

c = Handle('Рисунок_3')
c.draw()