#        key  >   value
dict1 = {'name': 'nika',
         'age': 16,
         'salary': 500000}
dict2 = {'name': 'sandro',
         'age': 25,
         'salary': 400000}
dict3 = {'name': 'vako',
         'age': 18,
         'salary': 20000}
dict4 = {'name': 'saba',
         'age': 19,
         'salary': 30000}


list1 = []
list2 = []
list3 = []
list4 = []


for key, value in dict1.items():
    list1.append(value)

for key, value in dict2.items():
    list2.append(value)

for key, value in dict3.items():
    list3.append(value)

for key, value in dict4.items():
    list4.append(value)


joined_list = list1 + list2 + list3 + list4
print(joined_list)