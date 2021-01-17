# The upper() and lower() string methods return a new string where all the letters in the original string have
# been converted to uppercase or lowercase,
spam = 'HELLO, world!'
print(spam.lower())
print(spam.upper())
print(f"Orginal String: {spam}")

# If you want to change the original string, you have to call upper() or lower() on the string and then assign the new string to
# the variable where the original was stored.
spam = spam.upper()
print(f"New string with new value in CAPS:{spam}")


# isupper() and islower() methods will return a Boolean True value if the string has at least one letter and all the letters are
# uppercase or lowercase, respectively
print(spam.isupper())  # Returns True or false
new_value = "Hello"
print(new_value.islower())


# isalpha() Returns True if the string consists only of letters and isn’t blank
print("hello".isalpha())
print("hello123".isalpha())
# isalnum() Returns True if the string consists only of letters and numbers and is not blank
print("hello123".isalnum())
# isdecimal() Returns True if the string consists only of numeric characters and is not blank
print('123'.isdecimal())
print('123A'.isdecimal())
# isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
print(" ".isspace())
print(", ".isspace())
# istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by
# only lowercase letters
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())  # not starts with lower letter

# startswith() and endswith() Methods
print('Hello, world!'.startswith('Hello'))
print('abc123'.endswith('12'))
print('abc123'.endswith('123'))

# Justifying Text with the rjust(), ljust(), and center() Methods
# 'Hello'.rjust(10) says that we want to right-justify 'Hello' in a string of total length 10. 'Hello' is five
# characters, so five spaces will be added to its left, giving us a string of 10 characters with 'Hello' justified right
print('Hello'.rjust(10))
print('Hello'.rjust(10, "*"))

print("HELLo".ljust(20, "*"))
print("HELLO".center(15, "="))
