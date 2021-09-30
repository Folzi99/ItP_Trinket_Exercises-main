#Write a Python program to compute the area of a disk. Prompt the user to enter the radius and print a nice message back to the user with the answer
import math

user = input("Radisu of disk: ")
radius = float(user)
answer = round(math.pi * radius ** 2, 3)

print('Radius of disck is:', answer)
