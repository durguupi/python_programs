names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
new_value_zipped = zip(names, heros)
print(list(new_value_zipped))
new_value = {}
# Using normal for loops we got new value with names:heros
for name, hero in zip(names, heros):
    new_value[name] = hero
print(new_value)

# Using dictionary comprehensions we can get with names:values without peter value
new_value_comp = {name: hero for name,
                  hero in zip(names, heros) if name != 'Peter'}
print(f"Output using dictionarycomprehension: {new_value_comp}")
