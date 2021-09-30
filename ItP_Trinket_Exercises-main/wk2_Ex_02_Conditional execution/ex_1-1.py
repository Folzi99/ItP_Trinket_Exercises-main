# Write a program that ask the user for an integer.
# If it is an even number, the program will print out that is is an even number.
# Otherwise it will print out that it is not.

user = input('Enter Number: ')

if int(user) % 2 == 0:
    print('That is an even number')
else:
    print('That is an odd number')
