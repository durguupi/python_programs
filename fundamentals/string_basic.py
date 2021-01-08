# This program says hello and asks for my name.
print("Hello World !")
print("What is your name")
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
# The len() function takes a string and evaluates to an int of the number of characters in the string.
print(len(myName))
print("What is your age ?")
age = int(input())
# input function will always return a string even if user typed integer
# The int(), float(), and str() functions will evaluate to the integer, floating-point number, and string
# versions of the value passed to them.
print("You will be " + str(age + 1) + " in a year")
