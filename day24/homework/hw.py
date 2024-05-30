list = [1, 2, 3, True, False, 1.5, 3.14, 5]
list1 = []
for i in list:
    if i.is_integer():
        list1.append(i)
print(sum(list1))