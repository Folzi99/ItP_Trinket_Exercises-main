# Write a program in which the user will try to guess an integer between 0 and 10. The user will have 3 guesses, if the guess is right, the program congratulates them and stop, if wrong the program will ask again until the number of guesses is used up. See 2 example outputs below.

# Hint: You need some functions from the random module... so you need to import it!

# Enter your guess (integer only) 1
# No, try again!
# Enter your guess (integer only) 2
# No, try again!
# Enter your guess (integer only) 3
# No, try again!
# Too bad, the number was: 9

# inter your guess (integer only) 2
# No, try again!
# Enter your guess (integer only) 5
# Congrats!

import random

random_int = random.randint(0, 9)
print(random_int)

user_guess = int(input("Enter your guess (integer only) "))
max_attempts = 3
attempts = 1

while attempts < max_attempts and user_guess != random_int:
    user_guess = int(input("Enter your guess (integer only) "))
    print("No, try again!")
    attempts += 1

if user_guess != random_int:
    print("Too bad, the number was: ", random_int)
else:
    print("Congrats!")