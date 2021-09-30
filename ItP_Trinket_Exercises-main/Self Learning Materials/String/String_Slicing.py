# We can also use the slice operator. Removing the n first or last element of a sequence is easy:
original_list = [0,1,2,3,4,5]

# create a new list with the same elements except the first 2 removed
result_list = original_list[2:]
print(result_list)

# create a new list with the same elements except the last 3 removed
result_list = original_list[:-3]
print(result_list)

# create a new list with the same elements except the first 1 and the last 2 removed
result_list = original_list[1:-2]
print(result_list)

# Removing one element (or several consecutive ones) is a bit more tricky. We need to get all the elements before and concatenate then to all the element after. See for example:

str = "Engineering"

print ("Original string: " + str)

# Removing char at pos 3
# using slice + concatenation
res_str = str[:2] +  str[3:]

print ("String after removal of character: " + res_str)
