def palcheck (word):
    if (word[::-1]).lower() == word. lower():
        print(True)
    else:
        print(False)
palcheck('gio')