## Update your program so that it handles wrong types of input without crashing, for example:
# please enter a float number (just press enter to finish) 2
# please enter a float number (just press enter to finish) hello
# Only floats!
# please enter a float number (just press enter to finish) 4.2
# please enter a float number (just press enter to finish)

# [2.0, 4.2] has 2 elements
# min:2, max:4.2, sum:6.2, average:3.1

num_list = []
elements = 0
str_num = 0

while str_num != "":
    str_num = input("please enter a float number(just press enter to finish) ")
    try:
        if str_num != "":
            num_list.append(float(str_num))
        elements = elements + 1
    except:
        print("only floats!")

avg_list = sum(num_list) / len(num_list)
print(f"{num_list} has {elements} elements")
print(f"min: {min(num_list)}, max: {max(num_list)}, average: {round(avg_list, 4)}")
