list1 = [1, 2, 3, 4, 5, 6]

# Using normal for loop function
my_list = []
for n in list1:
    my_list.append(n)
print(my_list)

# Using list comprehension
my_list_com = [n for n in list1]
print(f"Output using list comprehension: {my_list_com}")

# To square the given number using the for loop
list_squ = []
for n in list1:
    list_squ.append(n * n)
print(list_squ)

# Using list comprehension
list_squ_com = [n * n for n in list1]
print(f"Output using list comprehension: {list_squ_com}")

# To get only the even values in the given list
even_list = []
for n in list1:
    if n % 2 == 0:
        even_list.append(n)
print(even_list)

# Using list comprehension
even_list_comp = [n for n in list1 if n % 2 == 0]
print(f"Output using list comprehension: {even_list_comp}")

# letter and number pair abcd and number pair of 0123
let_num = []
for letter in 'abcd':
    for num in range(4):
        let_num.append((letter, num))
print(let_num)

# Using list comprehension how we can print the same loop
let_num_comp = [(letter, num) for letter in 'abcd' for num in range(4)]
print(f"Output using list comprehension: {let_num_comp}")
