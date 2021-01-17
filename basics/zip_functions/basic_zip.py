# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
# The iterator stops when the shortest input iterable is exhausted.
# With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
# tHis prints the iterator object memory location
print(zipped)
# To retrieve the final list object, you need to use list() to consume the iterator.
print(list(zipped))
