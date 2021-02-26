# Reference : https://www.youtube.com/watch?v=B5GhlXhDfoE&ab_channel=MikeDane
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def grid_call(index_value):

    for row in grid:
        for col in row[index_value]:
            # It will print al the elements
            print(col, end="")
            # print(col, end=" ") # To have space between 0
    print()


index_value = 0
while index_value < 6:
    grid_call(index_value)
    index_value += 1
