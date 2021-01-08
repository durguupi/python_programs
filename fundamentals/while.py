# While condition executes untill the condtion is true
# The code in a while clause will be executed as long as the while statement’s condition is True
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1


# There is a shortcut to getting the program execution to break out of a while loop’s clause early. If the
# execution reaches a break statement, it immediately exits the while loop’s clause
# If the user enters any name besides Joe, the continue statement causes the program execution to jump
# back to the start of the loop
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
