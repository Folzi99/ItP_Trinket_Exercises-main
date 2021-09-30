# It is quite similar as with list. Note that we work on substring not just character.
## the in operator returns True if the substring is found at least once in the list
## the find method returns the (positive) index of the first occurence of the substring. If the element cannot be found it will return -1. Note that a "rfind" version of this method allows you to find the index of the last occurrence (the first one from the right ==> rfind).

my_string = "Hello world!"
if "Hello" in my_string:
    print("Hello is in ", my_string)
if "World" not in my_string:
    print("World is NOT in ", my_string)


print("world can be found at index:", my_string.find("world"))
print("hello cannot be found, we get the return:", my_string.find("hello"))