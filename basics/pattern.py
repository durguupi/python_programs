# Write a Python program to construct the following pattern, using a nested for loop.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
star = '*'

for pattern in range(0, 5):
    print(star)
    star += " *"

reverse_star = "* * * *"

for star in range(0, 4):
    print(reverse_star)
    reverse_star = reverse_star[:-2]
