import random
numberOfStreaks = 0
list_value = ['H', 'T']
random_out = ''
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    random_result = random.choice(list_value)
    random_out += random_result
print(random_out)
print(random_out.count('HHHHHH'))
print(random_out.count('TTTTTT'))
numberOfStreaks = random_out.count('HHHHHH') + random_out.count('TTTTTT')
print(numberOfStreaks)
# Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
