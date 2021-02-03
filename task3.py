class Cell:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        sum_number = self.number + other.number
        return sum_number

    def __sub__(self, other):
        dif = self.number - other.number
        if dif > 0:
            return dif
        else:
            raise ValueError("Недопустимая операция")

    def __mul__(self, other):
        mul = self.number * other.number
        return mul

    def __floordiv__(self, other):
        div = self.number // other.number
        return div

    @property
    def make_order(self):
        var_1 = self.number // 5
        var_2 = self.number % 5
        result = var_1 * "*****\n" + var_2 * "*"
        return result


cell_1 = Cell(5)
cell_2 = Cell(6)
print(cell_1 + cell_2)
# print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_2 // cell_1)
print(cell_2.make_order)
