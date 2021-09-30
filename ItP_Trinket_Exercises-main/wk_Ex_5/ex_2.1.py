# Write a program that will ask the user to enter some text. Then, it will show all the letters from that text but separated by a space, example output:
# please enter some text? hello world
# h e l l o   w o r l d

user = input("enter some text: ")

space = user.replace("", " ")

print(space)
