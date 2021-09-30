# Write a program with the following output. If you are stuck read the explanations below (but you should try to solve it by yourself first!).
# (A)
# (B)
# (B)
# (A)
# (B)
# (B)
# (A)
# (B)
# (B)

v = 0
while v == 0:
    print('(A)')
    v = 0 + 1
    print('(B)')

# SOLUTION
for i in range(3):
    print("(A)")
    for j in range(2):
        print("(B)")