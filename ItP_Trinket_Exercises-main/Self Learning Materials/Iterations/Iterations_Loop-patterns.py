# As you are discovering in this topic, loops can be used to do many repetitive things. The possibility are almost endless, but there is only a handful of type of loops or loop patterns. Here, we present some of the basic ones that you should be able to master quickly.

# While loop
## A pattern for a while loop that you should master early is when you want to iterate for a specific number of times.

# Let's say you want to create a macro for your favorite multiplayer FPS that will say "Fire in the hole! Go! Go! Go!". We need to 'print' a sentence and then 3 times 'Go!'. Here how we do it in Python with a while loop
## EX:
print("Fire in the hole!")
n = 0
while n <= 3:
    print("Go!")
    n = n + 1

# Pattern
# - Define a counting variable, usually starting at 0 (n below)
# - while this variable is less (or 'less-or-equal') to a specific value (or variable, max_repetition below)
# - Body of the while: what needs to be repeated
# - Update of the counting variable, it should be the last statement of the while body

## counter = 0
## max_repetition = 3
## while n <= max_repetition:
    ## while body
    ## n = n + 1

# First For loop pattern
## When we use a for loop we have used a list of names (see the 'Happy new year' example in the other trinket) and just before you saw how to do a while loop for a specific number of times. What if we could combine both so that we can do a for loop?

# Range function
## The range() function will help us to do a for loop for a specific number of times. This function creates a list of integer automatically for us, for example:
numbers = range(10)
print(numbers)
## EX
## Let's print all the numbers between 0 and 9 one by one using a for loop and a range function.
numbers = range(10)
for number in numbers:
    print(number)

# Range function (futher)
## You can see that we printed out all the number from 0 to 10 (excluded). range is actually more powerful, we can specify the start number, the end number (as we just did) and the step. For example, let's show all the integers from 0 to 10 (included) that are divisible by 2:
numbers = range(0, 11, 2)
for number in numbers:
    print(number)