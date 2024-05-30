integer_input = int(input('enter positive num: '))

list = []
for i in range(1, integer_input + 1):
    if integer_input % i == 0:
        list.append(i)
print(list)