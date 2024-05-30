fruits = [ 'apple' , 'orange' , 'pear' , 'kiwi' , 'Lemon']
print('Remember the fruit countdown starts from zero')
user_choice = int(input('which fruit do you want: '))

if user_choice >=0 and user_choice <=5:
    print('your fruit is: ' + str(fruits[user_choice]))
else:
    print('enter fruit number from 0 to 5')