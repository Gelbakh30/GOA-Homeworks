def sum_numbers(numbers):
    positive_sum = 0
    negative_count = 0
    
    for num in numbers:
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_count += 1
            
    print('Sum of positive numbers:', positive_sum)
    print('Number of negative numbers:', negative_count)

sum_numbers([1, -2, -6, -7, 7, 8, 9, 10, -1])