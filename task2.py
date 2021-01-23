import random

def random_list(number):
    my_list_1 = [random.randint(1,number) for i in range(15)]
    return my_list_1

if __name__ == "__main__":
    my_list_1 = random_list(1000)
    print(my_list_1)
    my_list_2 = [my_list_1[i] for i in range(1,15) if my_list_1[i]>my_list_1[i-1]]
    print(my_list_2)