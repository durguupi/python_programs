eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}

for key in eggs.keys():
    print(f"The key element present in dict is: {key}")

for val in eggs.values():
    print(f"The value element present in dict is: {val}")

for item in eggs.items():
    print(f"The items present in dict is: {item}")

for key, val in eggs.items():
    print(f"Key: {key}, Value: {val}")

# Printing the dict into list of keys
print(list(eggs.keys()))

# Printing the dict into list of values
print(list(eggs.values()))

print(list(eggs.items()))

# Checking Whether a Key or Value Exists in aDictionary
# Returns True of false based on the value present
print('name' in eggs.keys())
print('cat' in eggs.values())
