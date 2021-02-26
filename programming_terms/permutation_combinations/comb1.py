import itertools

list1 = [1, 2, 3, 4, 5, 6]

combinations = itertools.combinations(list1, 3)
# for com in combinations:
#     print(com)
# Now if I want to print sum of 10 combinations and order does not matter
# for com in combinations:
#     if sum(com) == 10:
#         print(com)
list_comp = [com for com in combinations if sum(com) == 10]
print(list_comp)
