# Traversing Lists in Parallel using for loop
# Python’s zip() function allows you to iterate in parallel over two or more iterables.
# Since zip() generates tuples, you can unpack these in the header of a for loop:
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
# for let, num in zip(letters, numbers):
#     print(f"Number: {num} Type: {type(num)}")
#     print(f"Letter: {let} Type: {type(let)}")

for let, num, oper in zip(letters, numbers, operators):
    print(
        f"Number: {num} Type: {type(num)} \nLetter: {let} Type: {type(let)} \nOperators: {oper} Type: {type(oper)}")
