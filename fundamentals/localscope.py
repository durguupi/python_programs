# Local Variables Cannot Be Used in the Global Scope
# The error happens because the eggs variable exists only in the local scope created when spam() is called
# Once the program execution returns from spam,that local scope is destroyed, and there is no longer a variable named eggs.
# So when your program tries to run print(eggs), Python gives you an error saying that eggs is not defined.
# def spam():
#     eggs = 31337
# spam()
# # it will retun error
# print(eggs)


# Local Scopes Cannot Use Variables in Other Local Scopes
# local variables in one function are completely separate from the local variables in another function
def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0


# this will return 99 since scope of eggs =0 ends in bacon() function so when the function call is over. it again goes to
# spam() function call and returns the value of eggs = 99
spam()
