# Write a program that allows your user to add two integers together, see the example output:

# let's do some addition
# What is the first operand 19
# What is the second operand 23
# 19 + 23 = 42

print("Let's do some addition!")
num_1 = int(input("What is the first operand? "))
num_2 = int(input("What is the second operand? "))

value = num_1 + num_2

print(f"{num_1} + {num_2} = {value}")