with open('task6.txt','r',encoding='utf-8') as ls:
    my_list = ls.readlines()
    salary = {}
    for i in my_list:
        str = i.split(':')
        name = str[0]
        temp_l = str[1].split()
        sal_temp = 0
        for j in temp_l:
            temp_p = j.split('(')
            for p in temp_p:
                if p.isdigit() == True:
                    sal_temp += int(p)
        salary[name] = sal_temp
    print(salary)


