import json


with open('task7.txt','r',encoding='utf-8') as f:
    firm_1 = f.readline()
    firm_1 = firm_1.split()
    firm_2 = f.readline()
    firm_2 = firm_2.split()
    firm_3 = f.readline()
    firm_3 = firm_3.split()
    firm_4 = f.readline()
    firm_4 = firm_4.split()
    firm_5 = f.readline()
    firm_5 = firm_5.split()
    firm_6 = f.readline()
    firm_6 = firm_6.split()
    firm_list = [firm_1,firm_2,firm_3,firm_4,firm_5,firm_6]
    sum_prof = 0
    prof_dict = {}
    damages_dict = {}
    average_dict = {}
    numbers = 0
    for i in firm_list:
        profit = int(i[2]) - int(i[3])
        if profit > 0:
            sum_prof += profit
            numbers += 1
            prof_dict[i[0]] = profit
        else:
            damages_dict[i[0]] = profit
    average_dict['average_profit'] = sum_prof/numbers
    result_list = [prof_dict,average_dict,damages_dict]
    with open('task7.json','w') as js:
        json.dump(result_list,js)
