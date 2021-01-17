my_list = []
while True:
    add_value = input("Введите элемент для добавления: ")
    if bool(add_value) == False:
        break
    else:
        my_list.append(add_value)
print(my_list)
list_range = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1
for i in range(1, list_range, 2):
    temp_value = my_list.pop(i)
    my_list.insert(i-1, temp_value)
print(my_list)
