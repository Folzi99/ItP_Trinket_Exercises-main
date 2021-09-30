# If it is an even number, the program will print out that is is an even number.
# If the integer is not even, it will print out that it is not
# *If the user does not input an integer, the program will show an error message to the user*

user = input('Enter Number: ')

try:
    if int(user) % 2 == 0 :
        print('That is an even number')
    else:
        print('That is an odd number')
except:
    print('Please enter an integer!')
