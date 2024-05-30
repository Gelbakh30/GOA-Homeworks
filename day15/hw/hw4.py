def find_min_max(num_list):
    min = num_list[0]
    max = num_list[0]

    for i in num_list:
        if min > i:
            min = i
            if max < i:
                max = i
        print(min,max)

        find_min_max(1,2,3,4,5)