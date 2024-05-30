nums = [1, 2, 3, 4, 5]
odd_nums = []
even_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

print(sum(even_nums), sum(odd_nums))