#REMINDER:
#   str3 = str1 + str2: str3 is a concatenation of the str1 and str2 strings
#   my_char = str1[0]: my_char takes the value of the first character of str1
#   sub_str = str1[0:1]: sub_str is a new string containing the first 2 characters of str1
#   my_length = len(str1); my_length take the value of the length of str1

#DIRECT MANIPULATION
# String methods are applied directly onto the string like this: str.method() and returns string based on str.
#   Methods like 'upper' and 'lower' allows you to change the character to upper case or lower case.'capitalize' allows you to capitalize each word.
#   'count' allows you to remove leading and ending empty spaces whereas 'lstrip' and 'rstip' remove the former and latter.

#ADVANCED MANIPULATION: split() and join()
# When accessing data, the format may not be convenient or we may need to pick only some of it. For that we will use the split function. It breaks a string into a list of words (or substrings). By default, any number of whitespace characters is considered a word boundary but you can define a boundary.
# Example:
da_string="Da ba dee da ba di"
da_list = da_string.split()
for word in da_list:
    print(word)

blue_string ="I have a blue house With a blue window blue is the colour of all that I wear blue are the streets And all the trees are too I have a girlfriend and she is so blue"
da_list = blue_string.split("blue")
for sub_string in da_list:
    print(sub_string)
    print("blue")

# Here is a more advanced yet very useful usage of split where we have a multi-line string divided into single lines:

song = """I have a blue house
With a blue window
Blue is the colour of all that I wear
Blue are the streets
And all the trees are too
I have a girlfriend and she is so blue"""
verse = song.split("\n")
for line in verse:
    print(line)

# Similarly, when we have data we will have to format it in a way that is convenient for the user to read on the screen or a file, or it may need to respect a specific format for a database. For that we will use the 'join' function. You choose a desired separator string, (offten called the glue) and join the list with the glue between each of the elements.Here is an example

words = ["red", "blue", "green"]
glue = ';'
s = glue.join(words)
print(s)
print("***".join(words))
print("".join(words))
