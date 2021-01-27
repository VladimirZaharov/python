from itertools import count,cycle
import task2

number = int(input('Введите начало отсчета: '))
last_number = int(input('Введите конец счета: '))
for i in count(start=number,step=1):
    print(i)
    if i == last_number:
        break

my_list_1 = task2.random_list(30)
for i in cycle(my_list_1):
    print(i)
    if i == 10:
        break
