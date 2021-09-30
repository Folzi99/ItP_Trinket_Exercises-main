## Write a program that will ask the user to enter several floats, then show various information as the output below.
# please enter a float number (just press enter to finish) 2.1
# please enter a float number (just press enter to finish) 4.2
# please enter a float number (just press enter to finish) 42
# please enter a float number (just press enter to finish)

# [2.1, 4.2, 42.0] has 3 elements
# min:2.1, max:42, sum:48.3, average:16.099999999999998)


num_list = []
elements = 0
str_num = 0

while str_num != "":
  str_num = input("please enter a float number(just press enter to finish) ")
  if str_num != "":
    num_list.append(float(str_num))
  elements = elements + 1
avg = sum(num_list) / len(num_list)
print(f"{num_list} has {elements} elements")
print(f"min: {min(num_list)}, max: {max(num_list)}, average: {round((avg), 4)}")
