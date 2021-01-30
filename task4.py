class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля - {self.speed}')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Скорость превышена")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Скорость превышена")


class PoliceCar(Car):
    pass


town_car = TownCar(65, 'Green', 'Toyota', False)
print(f'автомобиль - {town_car.name},цвет - {town_car.color}, движется со скоростью - {town_car.speed}')
town_car.show_speed()

police_car = PoliceCar(80, 'Yellow', 'Mazda', True)
police_car.go()
police_car.turn("налево")
police_car.stop()
