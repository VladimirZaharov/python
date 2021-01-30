class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname} на должности {self.position}')

    def get_total_income(self):
        print(f'полный доход составляет: {self._income["wage"] + self._income["bonus"]}')


a = Position('Иван', 'Иванов', 'директор', {'wage': 50000, 'bonus': 20000})
a.get_full_name()
a.get_total_income()
