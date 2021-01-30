class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки', end=" ")


class Pen(Stationery):

    def draw(self):
        super().draw()
        print("ручка")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print("карандаш")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print("маркер")


pen = Pen("var")
pen.draw()

pencil = Pencil('var')
pencil.draw()

handle = Handle('var')
handle.draw()




