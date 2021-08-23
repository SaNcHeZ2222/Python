class Cell:
    def __init__(self, q):
        self.quantity = q

    def __add__(self, other):
        print(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity >0:
            print(self.quantity - other.quantity)
        else:
            print('Начальная клетка будет уничтожена')

    def __mul__(self, other):
        print(self.quantity * other.quantity)

    def __floordiv__(self, other):
        print(self.quantity // other.quantity)

    def make_order(self, len_row):
        for i in range(1, self.quantity+1):
            if i % len_row == 0:
                print()
            else:
                print('*', end='')


a = Cell(20)
b = Cell(10)

a+b
print()

a-b
print()

a*b
print()

a//b
print()

a.make_order(8)

