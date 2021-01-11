var_int = input('Введите число: ')
var_int_2 = f'{var_int}{var_int}'
var_int_3 = f'{var_int_2}{var_int}'
print(int(var_int) + int(var_int_2) + int(var_int_3))