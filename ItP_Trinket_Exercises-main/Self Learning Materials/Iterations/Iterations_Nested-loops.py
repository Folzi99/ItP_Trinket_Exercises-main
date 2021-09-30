# Nested Loops
## When you have more advanced problems involving repetition within repetition you may need to use loops within loops or nested loops.

# Motivating example
## For example, a supermarket regional manager may need to check on stocks for each of the supermarket he/she supervises. For that, he/she will look at for each product stock at each store.. you can see 2 levels of iterations:
    # go through each store
    # go through each product (within a store) and that the "store loop" has to "include" the "product loop".
## Unfortunately, writing such a program is out of reach for the moment. Instead, we will go through a less 'authentic' example.

# EX
## Let's say, we want to see the divisors of all the integers between 0 and 10. We see that we will iterate over all those integers and for each integer will check if all the integers less than it are divisors of that integers. Here is how we do it with nested loops:

numbers = range(0,11)
# We go through all the numbers
for current_number in numbers:
    print("The divisors of", current_number, "are:")
    # we go through all the numbers between 0 and current_number
    for divisor in range(1,current_number+1):
    # if current_number is divisible by divisor
        if(current_number % divisor) == 0 :
            print(divisor)
# PRACTICE
## Modify the previous code so that:
## The program go through the numbers between 1 and 42
## The divisors to be tested are between 1 and 5

numbers = range(1,43)

for current_number in numbers:
    print("The divisors between 1 and 5 for", current_number, "are:")
    for divisor in range(1, 6):
        if(current_number % divisor) == 0 :
            print(divisor)