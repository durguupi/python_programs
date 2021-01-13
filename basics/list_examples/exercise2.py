# Write a Python program to count the number of strings where the string length is 2 or more and
# the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

sample_list = ['abc', 'xyz', 'aba', '1221']
count_items = 0
for items in sample_list:
    print(items)
    if len(items) >= 2 and items[0] == items[-1]:
        count_items += 1


print(f"Count of the items: {count_items}")
