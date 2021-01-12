a = int(input('Введите а: '))
b = int(input('Введите b: '))
count = 0
while a < b:
    a = a + a * 0.1
    count += 1
print(f'Спорстмен достиг результата в {b}км на {count} день')


