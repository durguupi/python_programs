# Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
new_string = "Python 3.2 "
numbers = sum(c.isdigit() for c in new_string)
letters = sum(c.isalpha() for c in new_string)
spaces = sum(c.isspace()for c in new_string)
print(f"Letters: {letters}")
print(f"Digits: {numbers}")
print(f"Spaces: {spaces}")
