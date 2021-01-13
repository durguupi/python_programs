# using ' ' * indent to print the correct amount of spaces of indentation. We don’t want to automatically print
# a newline after these spaces,so we also pass end=''
# If indentIncreasing is True, then we want to add one to indent. But once indent reaches 20,
# we want the indentation to decrease
import time
import sys
indent = 0  # How many spaces to indent.
indentIncreasing = True  # Whether the indentation is increasing or not.
try:
    while True:  # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)  # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
