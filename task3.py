'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
'''
season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {1:'зима', 2:'зима', 3:'весна',
               4:'весна', 5:'весна', 6:'лето',
               7:'лето', 8:'лето', 9:'осень',
               10:'осень', 11:'осень', 12:'зима'}
number = int(input('Введите номер месяца: '))
if number == 1 or number == 2 or number == 12:
    print(season_list[0])
elif number in range(3, 6):
    print(season_list[1])
elif number in range(6, 9):
    print(season_list[2])
elif number in range(9, 12):
    print(season_list[3])
else:
    print("Вы ввели неверное значение!")


print(season_dict.get(number))