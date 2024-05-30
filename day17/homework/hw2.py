def joining(words):
    i = int(input("which index do you want to remove: "))
    words[i] = "dog"
    " ".join(words)
    print(words)
joining(['luka', 'nika', 'giorgi', 'sandro'])