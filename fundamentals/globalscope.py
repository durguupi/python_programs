# Global Variables Can Be Read from a Local Scope
# Since there is no parameter named eggs or any code that assigns eggs a value in the spam() function,
# when eggs is used in spam(), Python considers it a reference to the global variable eggs.

def spam():
    # if eggs value is defined within local scope print statement takes this value and prints or else prints global value42
    # eggs = 10
    print(eggs)


eggs = 42
spam()
print(eggs)
