# Write a function that takes a list value as an argument and returns a string with all the items separated by
# a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the
# function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any
# list value passed to it. Be sure to test the case where an empty list [] is passed to your function

spam = ['apples', 'bananas', 'tofu', 'cats', 'elephant', '44']
# spam = []


def function1(list_value):
    len_list = len(list_value)
    if len_list == 0:
        print("and")
    else:
        print(f"{', '.join(list_value[:len_list -1])} and {list_value[-1]}")


function1(spam)
