## Write a program that ask the user to enter a float. From that the program will compute the integers directly below it and directly above it, then it will show these 2 integers. Hint: You need some functions from the math module... so you need to import it!
# what is your number? 42.42
# the closest integer below it is 42
# the closest integer above it is 43

import math

flo_user = float(input("What is your number? "))
int_above = int(math.ceil(flo_user))
int_below = int(math.floor(flo_user))

print(f"the closes integer below it is {int_below}", f"the closes integer below it is {int_above}", sep="\n")
