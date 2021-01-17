tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(list_value):
  # Iterate over each element and get its len() for comparison.
    maxCount = 0
    for lst in list_value:
        for elem in lst:
            maxCount = max(maxCount, len(elem))

    # print(maxCount)

    for lst1, lst2, lst3 in zip(list_value[0], list_value[1], list_value[2]):
        print(lst1.rjust(maxCount) + "" +
              lst2.rjust(maxCount) + "" + lst3.rjust(maxCount))


printTable(tableData)
