# Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
oddnum = 0
evennum = 0
for num in numbers:
    if num % 2 == 0:
        evennum += 1
    else:
        oddnum += 1
print(f"Number of even numbers : {evennum}")
print(f"Number of odd numbers : {oddnum}")

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num)
