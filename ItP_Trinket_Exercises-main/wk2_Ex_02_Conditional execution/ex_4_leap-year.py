## Write a program that ask the user to input a year and determines if it is a leap year. The program shows the result to the user. A year is a leap year when:

# It is divisible by 4
# **except** when it is also divisible by 100
# **except** if the year is divisible also by 400 (it is a leap year then)

# Some examples:
    # 1992 (divisible by 4 but not by 100) is a leap year
    # 2000 (divisible by 400) is a leap year
    # 1900 (divisible by 4 and 100 but not 400) is not a leap year
    # 2021 (not divisible by 4,100 or 400) is not a leap year


year = input("Enter a Year: ")
value = int(year)

if (value % 4 == 0):
    print(value, "is a leap year")
elif (value % 100 == 0):
    print(value, "is NOT a leap year")
elif (value % 400 == 0):
    print(value, "is a leap year")
else:
    print('This is not a leap year')

#SOLUTION
#get the year from the user and convert it to an integer
year = int(input("what is the year?"))

#we prepare some strings as we will reuse them
#note that we need to convert year
leap_year = str(year) + " is a leap year"
not_leap_year = str(year) + " is not a leap year"

#checking if it is a leap year
if (year % 4 ==0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(leap_year) # divisible by 4, 100 and 400, it is a leap year
        else:
            print(not_leap_year) # divisible by 4, 100 but not by 400 , it is NOT a leap year
    else:
        print(leap_year)# divisible by 4 but not by 100 , it is a leap year
else:
    print(not_leap_year) # NOT divisible by 4, it is NOT a leap year