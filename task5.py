my_list = [15, 13, 11, 8, 6, 4]
my_number = int(input('Введите число: '))
for i in range(len(my_list)):
    if my_number > my_list[i]:
        my_list.insert(i, my_number)
        break
    if i == len(my_list) - 1:
        my_list.append(my_number)
print(my_list)
