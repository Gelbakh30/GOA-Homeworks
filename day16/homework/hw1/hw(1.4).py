def func(number_list):
    sum = 0
    quantity = 0
    
    for num in number_list:
        if num >= 0:
            sum = sum + num
        else:
            quantity = quantity + 1
    
    print(sum,quantity)

func([1,2,3,-1,-2,-3])