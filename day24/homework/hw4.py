list = [1, 1, 1, 1, 3, 4, 5, 6, 3, 3, 3, 3, 3]
max_count = 0

for i in list:
    count = list.count(i) 
if count > max_count:
    max_count = count
print(max_count)