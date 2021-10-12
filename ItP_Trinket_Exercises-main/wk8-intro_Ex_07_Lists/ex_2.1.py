# Complete the code below to turn every item of a list into its square and print each one on one line (but not as a list), example output:
#   my_list is:  [1, 2, 3, 4, 5, 6, 7]
#   the squares are:1 4 9 16 25 36 49

my_list = [1, 2, 3, 4, 5, 6, 7]
print("my_list is: ", my_list)
print("the squares are:", end="")
for number in my_list:
    print(number*number, end=" ")
