# There is no quick and easy approach to remove a character from a string. Instead we have 'naive' approach that allows you to remove all occurrences of a character. It is specifically useful want you to clean some log files.
# NAIVE APPROACH
# Just traverse the string and create a new string one character at a time except when the non desired character is found.

input_str = "how'ya doin'mate?"

# Printing original string
print("Original string: " + input_str)

result_str = ""

for char in input_str:
    if char != "'":
        result_str = result_str + char

# Printing string after removal
print("String after removal of i'th character : " + result_str)

# Based on that, you can figure out how to remove substrings (that would require nested loops) or just 1 or n occurrences of a character (that would require a counter).
