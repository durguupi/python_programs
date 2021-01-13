# return means 'return and stop' whereas 'yield` means 'return, but continue
# Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory,
# they generate the values on the fly:

# Using print statement using return and using yield
print("Using print statement to loop and print the number")


def make_list_print(number):
    for num in range(number):
        print(f"Print Local variable num: {num}")


make_list_print(5)
print("Using return statement to loop and return the number")
# A return in a function is the end of the function execution, and a single value is given back to the caller.


def make_list_return(number):
    for num in range(number):
        return f"Return Local variable num: {num}"


print(make_list_return(5))
print("Using yield statement to loop and yield the number")
# Yield returns a generator object to the caller, and the execution of the code starts only when the generator is iterated.


def make_list_yield(number):
    for num in range(number):
        #print(f"Yield Local variable num:{num}")
        yield num


print(make_list_yield(5))  # returns the generator object
print(list(make_list_yield(8)))  # It will return all of the values

# this returns 0 as the next value from genreator object
yield_value = make_list_yield(5)
print(next(yield_value))
# this returns 1 as the next value from genreator object
print(next(yield_value))
print(next(yield_value))

for yield_v in make_list_yield(8):
    print(yield_v, end=", ")
