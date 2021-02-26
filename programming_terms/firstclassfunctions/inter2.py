def addr_func(x):
    def adder(y):
        return x + y
    return adder


# Now this add_15 is adder function so when we call that we have tp pass again variable which will be taken as y
add_15 = addr_func(5)

print(add_15(10))
