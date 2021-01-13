def spam():
    global eggs
    eggs = 'spam'  # this is the global


def bacon():
    eggs = 'bacon'  # this is a local


def ham():
    print(f"From ham function: {eggs}")  # this is the global


eggs = 42  # this is the global
# this will print 42 as ham considers the global variable of eggs as "42"
ham()
spam()
# this will print "spam" as spam function is executed and now global variable gets changed
ham()
print(eggs)
