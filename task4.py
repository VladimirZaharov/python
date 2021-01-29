with open('task4.txt', 'r',encoding='utf-8') as cnt:
    str_cnt = cnt.readline()
    with open('task4.1.txt', 'w',encoding='utf-8') as nc:
        nc.write(str_cnt.replace('One','Один'))
    str_cnt = cnt.readline()
    with open('task4.1.txt', 'a', encoding='utf-8') as nc:
        nc.write(str_cnt.replace('Two', 'Два'))
    str_cnt = cnt.readline()
    with open('task4.1.txt', 'a',encoding='utf-8') as nc:
        nc.write(str_cnt.replace('Three','Три'))
    str_cnt = cnt.readline()
    with open('task4.1.txt', 'a',encoding='utf-8') as nc:
        nc.write(str_cnt.replace('Four','Четыре'))
