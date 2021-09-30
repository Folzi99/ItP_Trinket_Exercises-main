# Update your exercise 6 program and change it so that you ask the user to input the number of seconds.

user = input('Enter a value >= 3600: ')
value = int(user)
hrs = value // 3600
mins = (value % 3600) // 60
secs = value % 60

print(f'Seconds: {value} = {hrs} Hour(s), {mins} minute(s), {secs} second(s).')

var = "12"
print(type(var))
print(var, "is ", type(var))
