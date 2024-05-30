string_list = []

for i in range(5):
    word = input("Please enter word: ")
    string_list.append(word)

join_char = input("Please enter char to join strings in list: ")

result = ""

for index in range(len(string_list)):
    if index % 2 == 0:
        result = result + string_list[index] + join_char

result = result[:-1]

print(result)
        