import copy
goods_list = []
number = 1
temp_dict = {"название": None, "цена": None, "количество": None, "ед": None}
while True:
    temp_dict["название"] = input('Введите название товара: ')
    temp_dict["цена"] = input('Введите цену на товар: ')
    temp_dict["количество"] = input('Введите количество товара: ')
    temp_dict["ед"] = input('Введите единицы измерения: ')
    temp_tuple = (number, copy.deepcopy(temp_dict))
    number += 1
    goods_list.append(copy.deepcopy(temp_tuple))
    resume = input("Добавить еще одну позицию? 'да' - для продолжения: ")
    if resume == "да":
        continue
    else:
        break

print(goods_list)


name_list = []
price_list = []
quantity_list = []
measure_list = []

for i in range(len(goods_list)):
    name_list.append(goods_list[i][1]['название'])
    price_list.append(goods_list[i][1]['цена'])
    quantity_list.append(goods_list[i][1]['количество'])
    measure_list.append(goods_list[i][1]['ед'])
stat_dict = dict(название=name_list, цена=price_list, количество=quantity_list, ед=measure_list)
print(stat_dict)
