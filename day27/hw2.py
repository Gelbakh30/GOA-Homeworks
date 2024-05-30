def capitalize_sentence(sentence):
    words = sentence.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    capitalized_sentence = ' '.join(words)
    return capitalized_sentence
print(capitalize_sentence("goa is best academy in the world"))