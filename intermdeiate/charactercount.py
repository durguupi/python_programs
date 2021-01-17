import pprint

# The pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries.
# the pprint() and pformat() functions that will “pretty print” a dictionary’s values.

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count_value = {}
# The program loops over each character in the message variable’s string, counting how often each character appears.
# The setdefault() method call ensures that the key is in the count dictionary (with a default value of 0)
# so the program doesn’t throw a KeyError error when count[character] = count[character] + 1 is executed


for character in message:
    count_value.setdefault(character, 0)
    count_value[character] = count_value[character] + 1

print(pprint.pprint(count_value))
