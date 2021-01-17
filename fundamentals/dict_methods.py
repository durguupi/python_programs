# dictionaries have a get() method that takes two arguments: the key of the value to retrieve and a fallback value to
# return if that key does not exist

picnicItems = {'apples': 5, 'cups': 2}
# Here we have value for cups key so we take that print it as 2
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# In this case there is no key in the name f eggs so instead of returing error. It enters default fallback value of 0
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# The setdefault() Method
# if there is no key present in dict we can add it by using the below code
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

# The setdefault() method offers a way to do this in one line of code.The first argument passed to the method is
# the key to check for, and the second argument is the value to set at that key
# if the key does not exist. If the key does exist, the setdefault() method returns the key’s value

# This will print black since the key is already present
print(spam.setdefault('color', 'white'))
# This will add white since the key is not present
print(spam.setdefault('color_add', 'white'))
# This prints the updated dictionary items with values
print(spam)
