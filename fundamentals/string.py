# String data types
print("Hello World !")
print('You can print the statement in single quotes as well')
print('Multiple statements:\nHello Python\nIts fun to learn you')
print("Alice is " + str(42) + " years of age")
##################################String concatenation################################################

print("Alice" + "Bob")
# if we use integer with string concatenation it will throw error
# TypeError: can only concatenate str (not "int") to str
#print("Alice" + 42 + "years of age")
print("Alice is " + str(42) + " years of age")
################################## String replication################################################

print("Alice " * 5)
# This will throw error replication is possible with both numbers or one string and number
# TypeError: can't multiply sequence by non-int of type 'str'
# print("Alice" * "Bob")
# print("Alice" * 5.0) # typeError: can't multiply sequence by non-int of type 'float'
print(5 * 2)

print(str(100))
print(str(-3.1111))
