def int_func(word):
    return word.title()

user_string = "jfsl jfslh rij lskkn lkjs"
user_list = user_string.split()
result = list(map(int_func, user_list))
for i in result:
    print(i, end=" ")