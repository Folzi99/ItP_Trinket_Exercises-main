# Write a program that asks the user to give the length of three sides (integer) of a triangle. Then it will determine whether the triangle is right-angled. Assume that the third entry is always the longest side. The program will show whether it is a right-angled triangle.

## Hint 1
# Floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for (strict) equality. Instead you should check if the difference between the 2 numbers is very small
# Also you do not know which of the 2 numbers (of the non hypotenuse sides) is the larger one so you should consider the absolute value of the difference (use the "abs()" function).
# All-in-all your condition that would be a condition written like this:
# abs(x-y) < 0.001

## Hint 2
# Note that your formula/expression is a little more complicated
# You also may want to store the result of your expression to make your program easier to read.

side_a = 3 #input("Enter Side 1: ")
side_b = 4 #input("Enter Side 2: ")
hypot = 5 #input("Enter Hypotenuse: ")

side_a2 = int(side_a) ** 2
side_b2 = int(side_b) ** 2
hypot2 = int(hypot) ** 2
print(side_a2,side_b2,hypot2)

try:
    if side_a2 + side_b2 == hypot2:
        print("This is a right-angled triangle")
    else:
        if side_a2 + side_b2 != hypot2:
            print("This is not a right-angled triangle")
except:
    print("Numbers only please")

#SOLUTION
#get the integers from the user
#we combine the int and the input functions to directly store integer values
side1 = int(input(" what is the first side of the triangle?"))
side2 = int(input(" what is the second side of the triangle?"))
hypo  = int(input(" what is the hypothenuse of the triangle?"))

#We check if the triangle is righ-angled
difference = abs((side1*side1) + (side2*side2) - (hypo*hypo))

    #due to number representation in the computer the difference is likely to be slightly above 0 so we check that it is very small
if  difference < 0.001:
    print("It is a right-angled triangle!")
else:
    print("It is NOT a right-angled triangle!")