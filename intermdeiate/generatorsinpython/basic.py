def square_numbers(nums):
    result = []
    for num in nums:
        result.append(num * num)
    return result


new_nums = square_numbers([1, 2, 3, 4, 5])
print(new_nums)

# Using list comprehensions
new_nums_comp = [n * n for n in [1, 2, 3, 4, 5]]
print(f"Output using list comprehensions: {new_nums_comp}")

# Now the same above function using generators can be written as below


def square_numbers_gen(nums):
    for num in nums:
        yield num * num


# This wil return just object location of generators.
# print(square_numbers_gen([1, 2, 3]))
gen_value = square_numbers_gen([1, 2, 3, 4, 5])
# Generators doesnt hold whole output in memory. It yields one result at time

# If you want all to be printed in one line then wrap it up with list. But we will lose the preformance
# print(f"Using list outputting all generators: {list(gen_value)}")

# This just returns the first object which is 1
print(next(gen_value))
print(next(gen_value))  # It will return again the next value which is 4

# This can be printed using for loop. It will print all the values
for value in gen_value:
    print(value)
