# Functions can return another function: Because functions are objects we can return a function from another function.

def log_message(msg):
    def logger():
        print(f"Logmessage: {msg}")
    return logger


log_message('Hiii') # It doesnt print anything because the functions returns value so it should be passed to variable
log_value = log_message('Hello')

log_value()
