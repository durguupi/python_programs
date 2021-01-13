
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'
# ================================================solution============================================================
def string_times(str, n):
    return str * n


print(string_times('Hi', 2))

# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;

# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'

# ================================================solution============================================================


def front_times(str, n):
    if len(str) < 3:
        return str * n
    else:
        return str[:3] * n


print(front_times('Chocolate', 3))

# Given a string, return a string where for every char in the original, there are two chars.
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'
# ================================================solution============================================================


def double_char(str):
    new_char = ""
    for char in str:
        new_char += char * 2
    return new_char


print(double_char('Hi-There'))
