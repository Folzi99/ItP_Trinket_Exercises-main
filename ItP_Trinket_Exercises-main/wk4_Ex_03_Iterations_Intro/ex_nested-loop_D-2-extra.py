# if you have trouble with coming up with a solution, here is a breakdown of how one could do it:

# What are the parts of this problem?
# Components: 2 type of printouts: (A) and (B)
# How many times we see those printouts?
# 3 times (A)
# 6 times (B)
# How do they relate?
# for each (A), we see 2 (B)
# Thus, we can assume that the (A) is in the outer loop and (B) in the nested loop
# Writing the parts of the solution
# Write 2 separate (not nested!) loops: one printing out (A) and another (B) so that you can have the output below:
# As we have a fixed number of (A) and (B) we will use for loops and range() function
# (A)
# (A)
# (A)
# (B)
# (B)
# (B)
# (B)
# (B)
# (B)
# Combine your parts into a full solution
# Put your (B) loop inside the (A) and update the range() function parameter for the (B) so that you match the expected output
