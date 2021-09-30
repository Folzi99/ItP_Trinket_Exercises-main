## Update the leap year program. With some or all the following requirements.

# If you used nested conditionals, use chained conditionals (and reciprocally).
# Manage non-integer input.
# Update your comments (if your original program did not have any, it should have had!).
# Use only one "if" (and "else"). For this one, your condition will be a  longer boolean expression that uses some logical operator.
# (**hard**) Use only two print statements.

#checking if it is a leap year
year = input("Enter a Year: ")
value = int(year)

if (value % 4 == 0):
    print(value, "is a leap year") # divisible by 400, it is a leap year
elif (value % 100 == 0):
    print(value, "is NOT a leap year") # divisible by 100 but not by 400, it is a NOT leap year
elif (value % 400 == 0):
    print(value, "is a leap year") # divisible by 4 but (not by 100 nor 400), it is a leap year
else:
    print(value 'is not a leap year') # NOT divisible by 4, it is NOT a leap year

# SOLUTION
#get the year from the user and convert it to an integer
year = int(input("what is the year?"))


#checking if it is a leap year
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    answer = str(year) + " is a leap year"
else:
    answer = str(year) + " is not a leap year"
print(answer)

# SOLUTION
#get the year from the user and convert it to an integer
year = int(input("what is the year?"))

#we prepare some strings as we will reuse them
#note that we need to convert year
leap_year = str(year) + " is a leap year"
not_leap_year = str(year) + " is not a leap year"

#checking if it is a leap year
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(leap_year)
else:
    print(not_leap_year)