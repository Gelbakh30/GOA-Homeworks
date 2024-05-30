name = input("please enter your password")
password = input("please enter your password:")
repeat_password = input("please enter your password again: ")

if password == repeat_password:
    print(name, "registered duccsesfully!")
else:
    print("Invalid password")