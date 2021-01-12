revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
result = revenue - costs
if result > 0:
    print("Предприятие приносит прибыль!")
elif result == 0:
    print('Предприятие вышло в ноль!')
else:
    print('Предприятие работает в убыток!')