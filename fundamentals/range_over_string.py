# Range function words only with integer
# to use range function within string we have to define our own method
# Print the range() over character or alphabet
# The ord() function returns the number representing the unicode code of a specified character.
print(ord('b'))

# yield function provides output and continue
# return function provides output and stop
# The chr() function returns the character that represents the specified unicode.


def character_range(char1, char2):
    for char in range(ord(char1), ord(char2) + 1):
        yield char


print(list(character_range('a', 'e')))
for letter in character_range('a', 'z'):
    print(chr(letter), end=", ")
