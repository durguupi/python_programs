# Combinations are groups of values where order does not matter
# Permutations are groups of values where order does matter
import itertools

list1 = [1, 2, 3]

combinations = itertools.combinations(list1, 2)
# print(combinations)
# So it will print only the values where order does not matter so it will print only (1,2)and not (2,1) as order does not matter
for comb in combinations:
    print(comb)
print("============================Permutations result================")
# But in permutation it will print all the combinations of values as order does matter
permutations = itertools.permutations(list1, 2)
for perm in permutations:
    print(perm)
