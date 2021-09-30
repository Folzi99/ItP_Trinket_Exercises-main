# Update your previous program so that:

# Show the index of each character below it.
# Show the reversed index of each character below it.
# You do not need to align properly indexes over 9.

user = "hello 47" #input("enter some text: ")
space = user.replace("", " ",)
f_count = user.count(0::)
r_count = user.count(::-1)

print(space, f_count, r_count, sep="\n")
