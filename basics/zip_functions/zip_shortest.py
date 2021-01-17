# # Passing Arguments of Unequal Length
# It’s possible that the iterables you pass in as arguments aren’t the same length.
# In these cases, the number of elements that zip() puts out will be equal to the length of the shortest iterable.

from itertools import zip_longest
# Since 5 is the length of the first (and shortest) range() object, zip() outputs a list of five tuples.
# There are still 95 unmatched elements from the second range() object.
# These are all ignored by zip() since there are no more elements from the first range() object to complete the pairs.

print(list(zip(range(5), range(100))))


# If trailing or unmatched values are important to you, then you can use itertools.zip_longest() instead of zip().
# With this function, the missing values will be replaced with whatever you pass to the fillvalue argument (defaults to None).
# The iteration will continue until the longest iterable is exhausted

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
# [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]
print(list(zipped))
