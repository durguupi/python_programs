# Although passing around references is often the handiest way to deal with lists and dictionaries, if the
# function modifies the list or dictionary that is passed, you may not want these changes in the original list or
# dictionary value.
#
# For this, Python provides a module named copy that provides both the copy() and deepcopy()
# functions. The first of these, copy.copy(), can be used to make a duplicate copy of a mutable value like a list or
# dictionary, not just a copy of a reference
import copy
spam = ['A', 'B', 'C', 'D']
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese))  # cheese is a different list with different identity.
cheese[1] = 42
print(spam)
print(cheese)
# cheese = copy.copy(spam) creates a second list that can be modified independently of the first.
