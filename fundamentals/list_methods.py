# List is mutable data type
# Finding a Value in a List with the index() Method
spam_new = ['hello', 'hi', 'howdy', 'heyas']
print(
    f"This prints the index value of the howdy in list: {spam_new.index('howdy')}")
print(f"This prints the index value of the hi in list: {spam_new.index('hi')}")


# Adding Values to Lists with the append() and insert() Methods
# append() method call adds the argument to the end of the list
spam_new.append('moose')
print(f"After appending the value: {spam_new}")
# The insert() method can insert a value at any index in the list
spam_new.insert(1, 'chicken')
print(f"After inserting the value: {spam_new}")

# Removing Values from Lists with the remove() Method
spam_new.remove('howdy')
print(f"After removing the value howdy: {spam_new}")
# If the value appears multiple times in the list, only the first instance of the value will be removed
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(
    f"After removing the value cat(only first occurence will be removed): {spam}")


# Sorting the Values in a List with the sort() Method
spam_int = [2, 5, 3.14, 1, -7]
spam_int.sort()
print(f"The sorted list of integer in spam_int: {spam_int}")
spam_string = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam_string.sort()
print(f"The sorted list of string in spam_string: {spam_string}")
# to print in reverse order use (reverse=True)
spam_string.sort(reverse=True)
print(f"The reverse sorted list of string in spam_string: {spam_string}")

# # Sort cant be done with list which has integer and string. It will result in typeerror
# spam_int_str = [1, 3, 2, 4, 'Alice', 'Bob']
# spam_int_str.sort()
# # TypeError: '<' not supported between instances of 'str' and 'int
# print(spam_int_str)

# ASCIIbetical order :rather than actual alphabetical order for sorting strings.
# This means uppercase letters come before lowercase letters
spam_ascii = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam_ascii.sort()
print(f"ASCIIbetical order of sorting: {spam_ascii}")
# to sort the values in regular alphabetical order, pass str.lower
spam_ascii.sort(key=str.lower)
# This causes the sort() function to treat all the items in the list as if they were lowercase without actually
# changing the values in the lis
print(f"ASCIIbetical order of sorting: {spam_ascii}")


# Reversing the Values in a List with the reverse() Method
spam_reverse = ['cat', 'dog', 'moose']
spam_reverse.reverse()
print(f"Reversing the order of list: {spam_reverse}")
