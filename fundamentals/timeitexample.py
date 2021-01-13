
# timeit() method is available with python library timeit.
# It is used to get the execution time taken for the small code given
# testing timeit()
# timeit.timeit(stmt, setup,timer, number)
# import timeit
# print(timeit.timeit('output = 10*5'))
# Import timeit module
import timeit


def func1():
    return 1


def func2():
    return sum([-1, 0, 1, 1])


# Test methods.
print(func1())
print(func2())

# Pass setup argument to call methods.
print(timeit.repeat("func1()", setup="from __main__ import func1"))
print(timeit.repeat("func2()", setup="from __main__ import func2"))
