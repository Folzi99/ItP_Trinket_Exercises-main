
# If you used chained conditionals, do the same with nested conditionals. If you used nested conditionals, do the same with chained conditionals.

try:
    grade = float(input("Enter Grade: "))
    if grade < 50:
        print("Fail")
    else:
        if grade < 60:
            print("Pass")
        else:
            if grade < 70:
                print("Credit")
            else:
                if grade < 80:
                    print("Distinction")
                else:
                    print("High Distinction")
except:
    print("that is not a number!")

# nested conditonals