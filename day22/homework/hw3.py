def manual_pop(list, index):
    new_list = []
    for i in list:
        if i != list[index]:
            new_list.append(i)
    print(new_list)
manual_pop([1,2,3,4,5,6], 4)