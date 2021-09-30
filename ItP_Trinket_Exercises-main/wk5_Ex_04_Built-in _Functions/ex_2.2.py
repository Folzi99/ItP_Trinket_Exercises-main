# Extend your previous program so that the program also shows the factorials of the 2 integers.
# Wait for solution

import math

flo_user = float(input("What is your number? "))
int_above = int(math.ceil(flo_user))
int_below = int(math.floor(flo_user))

print(f"the closest integer below it is {int_below} with a factorial of {math.factorial(int_below)}", f"the closest integer below it is {int_above} with a factorial of {math.factorial(int_above)}", sep="\n")



