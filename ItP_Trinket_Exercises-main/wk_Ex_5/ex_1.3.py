# Write a function return the index of a letter within a string (-1 if cannot be found).

word = "supercalifragilisticexpialidocious"
count = 0

for letter in word:
    if letter == 'i':
        count = count + 1
print(count)
