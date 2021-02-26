word = '''As he crossed toward the pharmacy at the corner he involuntarily turned his head because of a burst of 
light that had ricocheted from his temple, and saw, with that quick smile with which we greet a rainbow or a rose, 
a blindingly white parallelogram of sky being unloaded from the van—a dresser with mirrors across which, 
as across a cinema screen, passed a flawlessly clear reflection of boughs sliding and swaying not arboreally, 
but with a human vacillation, produced by the nature of those who were carrying this sky, these boughs, this gliding façade.
As he crossed toward the pharmacy at the corner he involuntarily turned his head because of a burst of light that had ricocheted 
from his temple, and saw, with that quick smile with which we greet a rainbow or a rose, a blindingly white parallelogram of 
sky being unloaded from the van—a dresser with mirrors across which, as across a cinema screen, passed a flawlessly clear 
reflection of boughs sliding and swaying not arboreally, but with a human vacillation, produced by the nature of those 
who were carrying this sky, these boughs, this gliding façade.'''

counts = dict()
new_word = word.split()
# print(new_word)
for word in new_word:
    counts[word] = counts.get(word, 0) + 1
print(counts)
print(f"Printing the count of 'sky': {counts['sky']}")

# To find the largest number and the word
largest = 0
theword = ""
for key, value in counts.items():
    # print(key, value)
    if value > largest:
        largest = value
        theword = key
print(theword, largest)

# To print the top 10 most used words
lst = []
for key, value in counts.items():
    new_list = (value, key)
    lst.append(new_list)
# We got new list of tuple values
# print(lst)
# Now we are sorting the value with largest to smallest using sort method
lst = sorted(lst, reverse=True)
# We are printing the first 10 elements
for val, key in lst[:10]:
    print(key, val)
