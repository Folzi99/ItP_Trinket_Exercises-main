#If you need more practice, here are a few outputs that you can try to match

# Pattern 1:
# (1x (A), 2x (B), 2x (C)) x 3
print( '---- Pattern 1 ---')
for a in range(3):
    print('(A)')
    for b in range(2):
        print('(B)')
    for c in range(2):
        print('(C)')

# Pattern 2:
# (2x (B), 1x (A)) x 3
print('---- Pattern 2 ---')
for b in range(3):
    print('(B)')
    print('(B)')
    for a in range(1):
        print('(A)')
# SOLUTION
print("---Pattern 2 SOLUTION ---")
for b in range(3):
    for a in range(2):
        print("(B)")
    print("(A)")

# Pattern 3:
# (2x (A), 2x (B). 2x (C)) x 3
print('---- Pattern 3 ---')
for abc in range(3):
    for c in range(2):
        print('(A)')
    for b in range(2):
        print('(B)')
    for c in range(2):
        print('(C)')

# Pattern 4:
# (1x (A), 1x (B). 2x (C), 1x (B). 2x (C)) x 3
print('---- Pattern 4 ---')
for abc in range(3):
    for a in range(1):
        print('(A)')
    for b in range(2):
        print('(B)')
        for x in range(2):
            print('(C)')
