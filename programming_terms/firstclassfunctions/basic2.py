def square(num):
    return num * num


def cube(num):
    return num * num * num

# Here we are passing function as argument and list of numbers
# For each number in the list we are passing a function


def math_func(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = math_func(square, [1, 2, 3, 4, 5])
print(squares)

cubes = math_func(cube, [1, 2, 3, 4])
print(cubes)
