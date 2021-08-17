class Road:
    thickness = 0.005
    weight_1 = 25

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def running(self):
        print(f"{round(self._length * self._width * Road.thickness * Road.weight_1)} т.")


a = Road(20, 5000)
a.running()