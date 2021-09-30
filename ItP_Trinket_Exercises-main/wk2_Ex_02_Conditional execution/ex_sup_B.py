## Update your previous program for 2 new features.
# (1) The user can input a float number.
# (2) If the input is not a number, the program will show an error message.

side1 = float(input(" what is the first side of the triangle? "))
side2 = float(input(" what is the second side of the triangle? "))
side3 = float(input(" what is the third side of the triangle? "))

if (side1 > side2 and side1 > side3):
    option1 = abs((side2 * side2) + (side3 * side3) - (side1 * side1))
    if option1 < 0.001:
        print("(A) It is a right-angled triangle!")
    else:
        print("(A) It is NOT right-angled triangle!")
elif (side2 > side3):
    option2 = abs((side1 * side1) + (side3 * side3) - (side2 * side2))
    if option2 < 0.001:
        print("(B) It is a right-angled triangle!")
    else:
        print("(B) It is NOT right-angled triangle!")
else:
    option3 = abs((side1 * side1) + (side2 * side2) - (side3 * side3))
    if option3 < 0.001:
        print("(C) It is a right-angled triangle!")
    else:
        print("(C) It is NOT right-angled triangle!")