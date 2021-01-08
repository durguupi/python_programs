# # what if you want to execute a block of code only a certain number of times go for loop
# print('My name is')
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')

# # Simple python program to find the sum from 1 to 100
# # Range function starts from 0 to end -1 i.e for to get 100 you should put 101 so 100 will be included
# total = 0
# for num in range(101):
#     total = total + num
# print(total)
###########################RANGE FUNCTION #######################
# The first argument will be where the for loop’s variable starts, and the second argument will be up to, but
# not including, the number to stop at.
print("Printing range")
for i in range(12, 15):
    print(i)
# Range with step fucntion
# The first two arguments will be the start and stop values, and the third will be the step argument.
print("Printing range fucntion and using step values")
for i in range(0, 10, 2):
    print(i, end=", ")
# Printing range function from postive to negative
print("\nPrinting range from Positive to Negative")
for num in range(2, -5, -1):
    print(num, end=", ")  # to print the outptut in one line
# Using range to print the numbers in reverse order
print("\nDisplaying a range of numbers by reverse order")
for i in range(10, 3, -1):
    print(i, end=', ')
# Use the reversed function to reverse range in Python
# always put the range function inside reversed
print("Printing reverse range using reversed()")
for num in reversed(range(0, 5)):
    print(num, end=", ")

# Converting range of numbers into list
print("\nConverting range of numbers into list of numbers")
print(list(range(0, 5)))
# Printing list in reverse order with range
print("Printing list in reverse order with range")
reversed_list = list(reversed(range(0, 10)))
print(reversed_list)

# Converting list of even numbers within 50 into list
print("Converting python range() to list of even and odd")
even_list = list(range(0, 50, 2))
print(f"Even list : {even_list}")

# Print the range() over character or alphabet
# The ord() function returns the number representing the unicode code of a specified character.
print(ord('b'))


def character_range(char1, char2):
    for char in range(ord(char1), ord(char2) + 1):
        yield char


for letter in character_range('a', 'z'):
    print(chr(letter), end=", ")
