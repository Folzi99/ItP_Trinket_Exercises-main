# Create a program that has an integer variable representing a number of seconds (choose a value > 3600).
# Convert it to hours, minutes, seconds and print out those to the use.
# For example: 3667 seconds is 1 hour(s), 1 minutes(s), 7 second(s).

value = 30662
hrs = value // 3600
mins = (value % 3600) // 60
secs = value % 60

print(f'Seconds: {value} = {hrs} Hour(s), {mins} minute(s), {secs} second(s).')
