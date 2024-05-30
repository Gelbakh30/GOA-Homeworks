odd_numbers = []
for i in range(30, 51):
    if i %2 != 0:
        odd_numbers.append(i)

multiples_of_three = []

for i in odd_numbers:
    if i %3 == 0:
        multiples_of_three.append(i)
print(multiples_of_three)