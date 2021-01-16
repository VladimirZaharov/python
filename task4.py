my_string = input('Введите текст: ')
my_list = my_string.split()
for n, i in enumerate(my_list, 1):
    print(n, i[:10])
