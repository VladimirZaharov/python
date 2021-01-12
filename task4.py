number = int(input('Введите число: '))
max = 0
while number != 0:
    temp_number = number - (int(number / 10) * 10)
    if temp_number > max:
        max = temp_number
    number = int(number / 10)
print(max)