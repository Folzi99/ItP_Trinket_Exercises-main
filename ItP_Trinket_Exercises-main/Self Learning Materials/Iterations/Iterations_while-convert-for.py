# Converting between for-loops and while-loops
#Sometimes it is useful to change the type of the loop. Also, understanding how for and while loops relate to each other should help you to understand the general concept of loop.
    ## A for loop might be easier to write but not so much to understand.
    ## Reciprocally, a while loop might be easier read/understand but not so much to program (cause you have to care of the loop variable initialization and update).

# In both case, we need to identify the following elements of the loop:
    ## Initial condition
    ## Loop body
    ## Variable update
    ## Termination condition
    ## for to while loop
    ## Initial for loop

# WHILE loop genericity
    ## The while is more generic than the for loop.
    ## Any for loop can be converted to a while
    ## A while loop may not possible to be converted to a for loop
    ## And/or it may be very complicated and unreadable)

# FOR to WHILE loop EX
## Inital FOR loop:
print("-- for implentation--")
# original for version
for i in range(1,10,2):
    print(i)
### Loop analysis
    ### Initial condition: i starts at 1
    ### Loop body: print(i)
    ### Variable update: i is increased by 2
    ### Termination condition: i is less than 10
# Result WHILE loop:
print("-- while implentation--")
# WHILE conversion
i=1
while i < 10:
    print(i)
    i = i + 2

# WHILE to FOR loop
## Initial while loop:
print("-- while implentation--")
# original while version
i=7
while i > 0:
    print(i*2)
    i = i - 1
### Loop analysis
    ### Initial condition: i starts at 7
    ### Loop body: print(i*2)
    ### Variable update: i is decreased by 1
    ### Termination condition: i is more than 0
# Result FOR loop
print("-- for implentation--")
# FOR conversion
for i in range(7,0,-1):
    print(i*2)

