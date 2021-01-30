class Road:

    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def weight(self):
        print(self._length * self._width * 25 * 5)

a = Road(156, 465)
a.weight()
