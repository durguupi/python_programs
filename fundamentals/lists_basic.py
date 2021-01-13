# Getting Individual Values in a List with Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])
print(spam[-1])  # to get the last value
# spam[2] is a list with an index (one integer).
# spam[1:4] is a list with a slice (two integers)
print(spam[2])
print(spam[1:3])  # prints index 1 and index 2 , ignores the last number
print(spam[:3])
print(spam[1:])  # prints all the values inculding index 1 to end
print(len(spam))
# # Indexes can be only integer values, not floats. The following example will cause a TypeError erro
# print(spam[1.0])
spam1 = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(f"The length of the spam1 list is: {len(spam1)}")
print(spam1[0])
print(spam1[0][1])  # to get the bat value
print(spam1[1][3])  # to get number 40

# Adding new values to list
spam1[1][3] = "hello"
print(f"The new value of spam1 list is: {spam1}")

# list values can change; that is, lists are mutable
spam_mutable = [0, 1, 2, 3, 4, 5]
cheese = spam_mutable  # The reference is being copied, not the list.
cheese[1] = 'Hello!'  # This changes the list value.
print(spam_mutable)
