user_word = input("Please enter uppercase word: ")

result = ''

for index in range(len(user_word)):
    if index % 2 == 0:
        result = result + user_word[index].upper()
    else:
        result = result + user_word[index].lower()

print(result)