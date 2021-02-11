import random
import copy
import time
from re import search


class Card:
    def __init__(self):
        random_number_list = [i for i in range(1, 91)]
        self.matrix = [sorted([random_number_list.pop(random.randint(0, len(random_number_list) - 1))
            for i in range(5)]) for n in range(3)]
        self.dist_matrix = []

    def check_number(self, barrel_var, user_answer):
        self.user_answer = user_answer
        self.barrel = barrel_var
        count = 0
        clone_matrix = copy.deepcopy(self.matrix)
        if search(r'\d+', str(clone_matrix)) is None:
            return 2
        for i in range(len(self.matrix)):
            if self.barrel in self.matrix[i]:
                self.matrix[i][self.matrix[i].index(self.barrel)] = '-'
            else:
                count += 1
        if count == 3 and self.user_answer == 'y':
            return 3
        elif count != 3 and self.user_answer == 'n':
            return 1
        elif self.user_answer != 'y' and self.user_answer != 'n':
            raise ValueError
        else:
            return self


    def __str__(self):
        self.dist_matrix = copy.deepcopy(self.matrix)
        for a in range(len(self.dist_matrix)):
            count = 0
            for b in range(len(self.dist_matrix[a])):
                if len(str(self.dist_matrix[a][b])) < 2:
                    self.dist_matrix[a][b] = f' {self.dist_matrix[a][b]}'
            while count != 4:
                count += 1
                self.dist_matrix[a].insert(random.randint(1, len(self.dist_matrix[a])), "  ")
        self.card_str = f'\n{" ".join(map(str, self.dist_matrix[0]))}' \
                        f'\n{" ".join(map(str, self.dist_matrix[1]))}' \
                        f'\n{" ".join(map(str, self.dist_matrix[2]))}\n'
        return f'{"-"*26}{self.card_str}{"-"*26}'


class UserCard(Card):
    def __init__(self, card_number):
        super().__init__()
        self.card_number = card_number

    def __str__(self):
        super().__str__()
        return f'{"-"*2}Ваша карточка номер  {self.card_number}{"-"*2}{self.card_str}{"-"*26}'


class CompCard(Card):
    def __str__(self):
        super().__str__()
        return f'{"-"*3}Карточка  компьютера{"-"*3}{self.card_str}{"-"*26}'


print('        Игра "Лото"')
time.sleep(2)
user_money = 1000
while user_money >= 0:
    user_card_1 = UserCard(1)
    user_card_2 = UserCard(2)
    user_card_3 = UserCard(3)
    comp_card = CompCard()
    print(f'У Вас {user_money} рублей на счету')
    cards_quantity = int(input('Сколько карт вы хотите взять? (не более трех)\nСтоимость одной - 50 рублей: '))
    bet = 50
    number_list = [i for i in range(1, 91)]
    user_money = user_money - bet * cards_quantity
    print(f'На кону {bet * cards_quantity + bet} рублей.\n')
    answer = 'n'
    while True:
        barrel = number_list.pop(random.randint(0, len(number_list) - 1))
        print(f'Новый бочонок:{barrel} (осталось: {len(number_list)})')
        if cards_quantity == 1:
            print(user_card_1)
        elif cards_quantity == 2:
            print(f'{user_card_1}\n{user_card_2}')
        elif cards_quantity == 3:
            print(f'{user_card_1}\n{user_card_2}\n{user_card_3}')
        print(f'\n \n {comp_card}')
        answer = input('Зачеркнуть цифру? (y/n) ')
        if cards_quantity == 1:
            func_answer_1 = user_card_1.check_number(barrel, answer)
            if func_answer_1 == 1:
                print(f'Цифра есть. Вы проиграли.(((')
                break
            elif func_answer_1 == 3:
                print('Цифры нет. Вы проиграли.(((')
                break
            elif func_answer_1 == 2:
                print('Вы выиграли!)))')
                user_money = user_money + 100
                break
        elif cards_quantity == 2:
            func_answer_1 = user_card_1.check_number(barrel, answer)
            func_answer_2 = user_card_2.check_number(barrel, answer)
            if func_answer_1 == 1 or func_answer_2 == 1:
                print(f'Цифра есть. Вы проиграли.(((')
                break
            elif func_answer_1 == 3 and func_answer_2 == 3:
                print('Цифры нет. Вы проиграли.(((')
                break
            elif func_answer_1 == 2 or func_answer_2 == 2:
                print('Вы выиграли!)))')
                user_money = user_money + 150
                break
        elif cards_quantity == 3:
            func_answer_1 = user_card_1.check_number(barrel, answer)
            func_answer_2 = user_card_2.check_number(barrel, answer)
            func_answer_3 = user_card_3.check_number(barrel, answer)
            if func_answer_1 == 1 or func_answer_2 == 1 or func_answer_3 == 1:
                print(f'Цифра есть. Вы проиграли.(((')
                break
            elif func_answer_1 == 3 and func_answer_2 == 3 and func_answer_3 == 3:
                print('Цифры нет. Вы проиграли.(((')
                break
            elif func_answer_1 == 2 or func_answer_2 == 2 or func_answer_3 == 2:
                print('Вы выиграли!)))')
                user_money = user_money + 200
                break
        if comp_card.check_number(barrel, answer) == 2:
            print('Вы проиграли.((( Компьютер закрыл все цифры.')
            break
print(f"Игра окончена. У вас {user_money} рублей.")
