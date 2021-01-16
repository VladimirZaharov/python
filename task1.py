list = []
print(list)
list.append(True)
list.append(100)
print(list)
another_list = [15.5, None, 'sample']
list.extend(another_list)
print(list)
for i in list:
    print(type(i))