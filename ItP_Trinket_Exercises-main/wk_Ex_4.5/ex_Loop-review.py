# Write a program that ask the user to enter grades.
# When the user enters "-1", the program will show the minimum, maximum, average grades.
# If the user enters something that is not a float, the program will crash (for now).
# See the output examples:
# what is the grade? 1
# what is the grade? 2
# what is the grade? 3
# what is the grade? -1
# what is the grade? -1
# no grade was input!

mark = 0

grade = [


while mark >= 0:
    mark = mark + 1
    print(input("what is the grade? "))
    if grade == " ":
        print("no grade was input!")
