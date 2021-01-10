# FIZZBUZZ game (Interview question)
for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FIZZBUZZ")
    elif number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0:
        print("BUZZ")
    else:
        print(number)

# FIZZBUZZ game (Interview question)
# Different online solution
stringy = ""
for number in range(1, 101):
    if (number % 3 == 0):
        stringy = "FIZZ"
    if number % 5 == 0:
        if (stringy == "FIZZ"):
            stringy += "BUZZ"
        else:
            stringy = "BUZZ"

    if stringy == "":
        print(number)
    else:
        print(stringy)
