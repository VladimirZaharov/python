with open('task3.txt', 'r', encoding='utf-8') as wrs:
    list_w = wrs.readlines()
    count_salary = 0
    print('Сотрудники с з\п больше 20000: ')
    for i in list_w:
        salary = i.split()
        count_salary += int(salary[1])
        if int(salary[1]) < 20000:
            print(salary[0])
    print(f'средняя з\п сотрудников - {count_salary/len(list_w)}')
