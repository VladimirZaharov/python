import task2


my_list_1 = task2.random_list(10)
print(my_list_1)

my_list_2 = [my_list_1[i] for i in range(15) if my_list_1[i] not in my_list_1[:i] and my_list_1[i] not in my_list_1[i+1:]]
print(my_list_2)