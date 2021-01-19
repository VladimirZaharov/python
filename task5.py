stop = 0
sum = 0
while stop != 1:
    user_str = input().split()
    for i in range(len(user_str)):
        if user_str[i] == 'q':
            stop = 1
            break
        try:
            sum += int(user_str[i])
        except ValueError:
            print("неверно введено значение")
    print(sum)
