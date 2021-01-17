# The join() method is useful when you have a list of strings that need to be joined together into a single string value.
# The join() method is called on a string, gets passed a list of strings, and returns a string.
# The returned string is the concatenation of each string in the passed-in list

list1 = ['cats', 'rats', 'bats']
print(','.join(list1))
print(' '.join(list1))
print(''.join(list1))
print('ABCD'.join(list1))

# The split() method does the opposite: It’s called on a string value and returns a list of string
# These whitespace characters are not included in the strings in the returned list.
# You can pass a delimiter string to the split() method to specify a different string to split upon
str1 = "My name is Simon"
print(str1.split())
print("H e-l-lo".split())
print("H-e-l-lo".split("-"))
print('MyABCnameABCisABCSimon'.split('ABC'))
