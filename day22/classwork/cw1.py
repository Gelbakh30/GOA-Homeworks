
def manual_pop(a):
    index = int(input("which index do you want to remove: "))
    for i in a:
        if i == index:
            a.pop(index)
    print(a)
manual_pop([1,2,3,4,5,6])