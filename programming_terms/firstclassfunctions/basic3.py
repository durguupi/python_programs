# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greeting(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function passed as an argument.")
    return greeting


print(greeting(shout))
print(greeting(whisper))


def greet(func, word):
    greeting = f'{func(word)} welcome to the python'
    return greeting


new_greet1 = greet(shout, 'Hello')
print(new_greet1)

new_greet2 = greet(whisper, "HIIII")
print(new_greet2)
