
def collatz(number):
    if number % 2 == 0:
        #print(number // 2)
        return number // 2
    else:
        #print(3 * number + 1)
        return 3 * number + 1


try:
    number = int(input("Enter Number: "))
    while True:
        output = collatz(number)
        print(output)
        if output != 1:
            number = output
        else:
            break
except ValueError:
    print('Error: You must enter integer')
