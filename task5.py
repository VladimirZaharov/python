import random


with open('task5.txt','w') as n:
    count = 0
    sum = 0
    while count != 10:
        number = random.randint(10,1000)
        n.write(f'{number} ')
        count += 1
        sum += number
    print(sum)

