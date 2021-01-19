def my_func(number_1, number_2):
    try:
        return int(number_1)/int(number_2)
    except ZeroDivisionError:
        print("Ошибка деления на ноль!")
    except ValueError:
        print("Введено не число!")
print(my_func(input('Введите первое число: '), input('Введите второе число: ')))