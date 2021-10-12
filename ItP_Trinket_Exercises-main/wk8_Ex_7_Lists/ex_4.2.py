# Did you test/debug your program?
#   Does it work for negative integers?
#   What happens with floats? strings?
#   Is there any number appearing twice in the list?
#       Can we show only the first occurence (reciprocally (depends on your original code) all occurences)? Extra: how would you do that (update your code in the pad below)?

list_numbers = [1, -2, 45, 77, 42, 109, -42, 56, 73, 32864, 154, -15612, 10, 100, 7895, 3, 42, 473, -152]

try:
    user = int(input("please enter a number: "))
    for number in list_numbers:
        if user in list_numbers:
            number = user
        print("Yay, we found:", user)
except:
    print("only integers!")

# SOLUTION

list_numbers = [1, -2, 45, 77, 42, 109, -42, 56, 73, 32864, 154, -15612, 10, 100, 7895, 3, 42, 473, -152]

try:
    user = 42# int(input("please enter a number: "))
    for number in list_numbers:
        if number == user:
            print("Yay, we found:", user)
except:
    print("only integers!")
