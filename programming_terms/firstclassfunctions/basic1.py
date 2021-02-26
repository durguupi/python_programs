# First-Class Functions" (FCF) are functions which are treated as so called "First-Class Citizens" (FCC).

# FCC's in a programming language are objects (using the term "objects" very freely here) which:

# Can be used as parameters
# Can be used as a return value
# Can be assigned to variables
# Can be stored in data structures such as hash tables, lists, ...
# Actually, very roughly and simply put, FCF's are variables of the type
# 'function' (or variables which point to a function). You can do with them everything you can do with a 'normal' variable.

def square(num):
    return num * num


f = square(5)
print(f)
# Now we are going to treat function as variables. Here we are assigning function to variable
fu1 = square
# Now we are calling that variable as functions.
print(fu1(5))

# Python program to illustrate functions can be treated as objects


def shout(text):
    return text.upper()


print(shout('hello'))
# Assigning functions as variable to yell
yell = shout
# Now calling that variable yell as function and passing the argument
print(yell('yelling'))
