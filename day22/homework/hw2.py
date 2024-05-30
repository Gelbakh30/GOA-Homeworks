def manual_min(list):
    min_list = list[0]
    for i in list:
        if i > min_list:
            min_list = i
    print(min_list)
manual_min([10,13,9,5])