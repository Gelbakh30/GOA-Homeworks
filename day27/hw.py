def num(list):
    nums = ()
    for i in list:
        if i.is_integer():
            nums.append(i * 2)
        else:
            nums.append(i * 4)
    print(nums)
num([2,2.5,4,6.5,8])