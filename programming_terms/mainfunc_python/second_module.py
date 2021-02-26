import first_module
# This will first print first module name since we are importing from that module and then it will print the below
# line of code
# We have defined if else condition in first module and only else condition will be run when we run this file
# Since this is not main method and we are importing from first_module
print(f"Second Module name: {__name__}")
