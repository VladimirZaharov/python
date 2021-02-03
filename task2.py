from abc import ABC, abstractmethod


class MyClass(ABC):

    @abstractmethod
    def cloth(self):
        pass


class Coat(MyClass):

    def __init__(self, v):
        self.v = v

    @property
    def cloth(self):
        result_c = self.v / 6.5 + 0.5
        return result_c


class Costume(MyClass):

    def __init__(self, h):
        self.h = h

    @property
    def cloth(self):
        result_cs = 2 * self.h + 0.3
        return result_cs


class Clothes:

    def __init__(self, v, h):
        self.coat = Coat(v)
        self.costume = Costume(h)

    @property
    def sum_cloth(self):
        sum_cl = self.coat.cloth + self.costume.cloth
        return sum_cl


clothes_1 = Coat(12)
clothes_2 = Costume(54)
sum_clothes = Clothes(12, 54)
print(clothes_1.cloth)
print(clothes_2.cloth)
print(sum_clothes.sum_cloth)
