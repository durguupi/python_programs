# Converting Types with the list() and tuple() Functions
number = 100
word = "Hello"
# converting to sting list and tuple
print(
    f"The converstion of {number} to string data type is: {str(number)} {type(number)}")

print(
    f"The converstion of {word} to list data type is: {list(word)} {type(word)}")
print(
    f"The converstion of {word} to list data type is: {tuple(word)} {type(word)}")
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
