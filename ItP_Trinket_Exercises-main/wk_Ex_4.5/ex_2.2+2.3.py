# We know want to manage not only addition but also subtraction, multiplication and addition. Let's break this problem in sub-problems ('divide-and-conquer' approach) and encode the solution in functions. First, we revise the previous program so that we have 2 functions (doing the same thing as previously):

# - A: a function that compute the addition of 2 numbers
# - B: a function that ask the user for 2 numbers, use the addition function and print out the result

print("Let's do some math!")
operator = input("enter operator [ + , - , /, *]: ")
num_1 = int(input("What is the first operand? "))
num_2 = int(input("What is the second operand? "))

if operator == "+":
    value = num_1 + num_2
elif operator == "-":
    value = num_1 - num_2
elif operator == "/":
    value = num_1 / num_2
else:
    value = num_1 * num_2

print(f"{num_1} {operator} {num_2} = {value}")