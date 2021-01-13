# On each iteration of the loop, enumerate() will return two values: the index of the item in the list,
# and the item in the list itself

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
