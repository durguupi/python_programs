# Tuple is immutable data type
# You can use tuples to convey to anyone reading your code that you don’t intend for that sequence of
# values to change. If you need an ordered sequence of values that never changes, use a tuple. A second benefit
# of using tuples instead of lists is that, because they are immutable and their contents don’t change,

eggs = ('hello', 42, 0.5, 100, 'less')
print(eggs)
print(type(eggs))
print(eggs[0])
print(eggs[:2])
print(len(eggs))
