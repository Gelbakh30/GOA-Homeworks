def manual_find(collection, find_item):
    for index in range(len(collection)):
        if collection[index] == find_item:
            return index
    return -1

print(manual_find([1,2,3,4,5], 8))