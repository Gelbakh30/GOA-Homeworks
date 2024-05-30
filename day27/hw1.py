def naames(names):

    converted_names = []
    for i in range(len(names)):
     if i % 2 == 0:
           converted_names.append(names[i].upper())
     else:
         converted_names.append(names[i].lower())

    print(converted_names)
naames(["vako", "nika", "luka", "sandro", "saba", "guga"])