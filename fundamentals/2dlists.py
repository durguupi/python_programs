# Reference : https://www.youtube.com/watch?v=B5GhlXhDfoE&ab_channel=MikeDane
number_grid = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]
# So think of first element in the box as row so [0] row and second one as column so [0]column of first row
# print(number_grid[row][col])
print(number_grid[0][0])

print(number_grid[3][3])  # 19

print(number_grid[3][4])  # last element

print(number_grid[1][2])  # 8

# Accessing using for loop to get the row values so here row is the index
for row in number_grid:
    print(f"The row of elements in number_grid is : {row}")


# Accessing using for loop to get the col values using nested for loops
# for row in number_grid:
#     for col in row:
#         # It will print al the elements
#         print(f"The column of elements in row is : {col}")
for row in number_grid:
    for col in row:
        # It will print al the elements
        print(col, end=" ")
    print()
