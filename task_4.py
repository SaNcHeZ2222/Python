class Car:
    def __init__(self, s, c, n, i=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if Car.show_speed(self) > 60:
            print(f'{self.name} превысила скорость!')


class SportCar(Car):
    def show_speed(self):
        print(f'{self.name} скорость {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if Car.show_speed(self) > 40:
            print(f'{self.name} превысила скорость!')


class PoliceCar(Car):
    def show_speed(self):
        print(f'{self.name} скорость {self.speed}')


a = TownCar(60, 'green', 'Toyota Prius')
a.show_speed()
a.go()
a.turn('направо')
a.turn('налево')
a.stop()

print()

b = TownCar(70, 'green', 'Toyota Prius')
b.show_speed()

print()

c = PoliceCar(70, 'black', 'Ford Police Responder', True)
c.go()
c.turn('направо')
c.turn('налево')
c.stop()

print()

d = SportCar(220, 'white', 'Nissan Skyline R34')
d.go()
d.show_speed()
d.turn('направо')
d.turn('налево')
d.stop()

print()

r = WorkCar(80, 'Red', 'KamaZ')
r.go()
r.show_speed()
r.turn('направо')
r.turn('налево')
r.stop()