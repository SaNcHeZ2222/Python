class Clothes:
    def __init__(self, name, size, height ):
        self.name = name
        self.size = size
        self.height = height

    @property
    def coat(self):
        return round((self.size/6.5 + 0.5), 2)

    @property
    def suit(self):
        return round((2*self.height + 0.3), 2)

a = Clothes('На Саню', 48, 170)
print(a.coat)
print(a.suit)