def likes(names):
    
    num_likes = len(names)

    if num_likes == 0:
        return "no one likes this"
    elif num_likes == 1:
        return names[0] + "like this"
    elif num_likes == 2:
        return names[0] + "and" + names[1] + "like this"
    elif num_likes == 3:
        return names[0] +"," + names[1] + "and" + names[2] + "like this"
    else:
        num_others = num_likes - 2
        return names[0] +"," + names[1] + "and" + str(num_others) + "others like this