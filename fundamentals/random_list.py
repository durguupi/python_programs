# Generating a List of numbers Using For Loop

import random
randomlist = []
for i in range(0, 5):
    n = random.randint(1, 30)
    randomlist.append(n)
print(randomlist)

# sample() method available in random module to directly generate a list of random numbers.
# Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(10, 30), 5)
print(f"The random list generated using sample method: {randomlist}")
print(random.choice(randomlist))
# The random.shuffle() function will reorder the items in a list
random.shuffle(randomlist)
print(randomlist)
