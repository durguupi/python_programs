# # Unzipping a Sequence
# how do you unzip Python objects ?
# Say you have a list of tuples and want to separate the elements of each tuple into independent sequences.
# To do this, you can use zip() along with the unpacking operator *,
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)
for num, let in pairs:
    print(f"{num}-->{let}")
