with open('task1.txt', 'a') as tx:
    tx.write('string five \nstring six \n')
    tx.seek(0)
with open('task1.txt', 'r') as tx:
    my_list = tx.readlines()
string_quantity = len(my_list)
print(f'количество строк в файле - {string_quantity}')
count = 1
for i in my_list:
    word_quantity = len(i.split())
    print(f'количество слов в {count} строке = {word_quantity}')
    count += 1
