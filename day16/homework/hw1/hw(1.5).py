def remove_spaces(word):
    word_without_space = ''
    
    for i in word:
        if i != " ":
            word_without_space = word_without_space + i
    
    print(word_without_space)

remove_spaces("vako gelbakhiani")