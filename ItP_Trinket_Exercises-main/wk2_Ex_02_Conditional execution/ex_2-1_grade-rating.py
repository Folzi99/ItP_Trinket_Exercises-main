#Write a program that ask the user to enter a grade. Depending on the user input, it will show the following:
## Grade < 50 : Fail
## 50<= Grade < 60 : Pass
## 60<= Grade < 70 : Credit
## 70<= Grade < 80 : Distinction
## 80<= Grade : High Distinction
## User entry is not a number : Not a number!

try:
    grade = float(input("Enter Grade: "))
    if grade < 50:
        print("Fail")
    elif grade < 60:
        print("Pass")
    elif grade < 70:
        print("Credit")
    elif grade < 80:
        print("Distinction")
    else:
        print("High Distinction")
except:
    print("that is not a number!")

# chained conditonals
