# Write a Python program to sum all the items in a list.
# Write a Python program to multiplies all the items in a list
import timeit
list1 = [1, 22, 55, 630, 88, 77]
list2 = [1, 2, 4, 3]


def sum_list(add):
    sum_list = 0
    for num in add:
        sum_list += num
    return sum_list


def multi_list(mul):
    multi_list = 1
    for num in mul:
        multi_list = num * multi_list
    return multi_list


print(f"Sum of all items in list: {sum_list(list1)}")
print(f"Multiply all items in list: {multi_list(list2)}")
print(f"Largest number in the list: {max(list1)}")
print(f"Smallest number in the list: {min(list1)}")
