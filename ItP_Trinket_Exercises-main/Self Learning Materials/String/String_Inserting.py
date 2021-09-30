# We cannot insert a substring or character into a string yet, we can create a string based on 2 other strings.
# The + (concatenate) operator allows you to concatenate two strings to obtain a new one.
# The [] (slice operator) combined with the + allows more flexibility

print ("using + only")
str1 = "Hello"
str2 = "world!"
str3 = str1 + str2
print ("string1: ", str1)
print ("string2: ", str2)
print ("string3 = str1 + str2: ", str3)

print ("using + only and []")
str4 = str3[:5] + " " + str3[5:]
print ("string4 = str3[:5] + " " + str3[5:]: ", str4)