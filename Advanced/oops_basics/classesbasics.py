#  Classes allow us to logically group our data and functions in a way that is easy to reuse and also easy to build
# upon if need be
# Class is blueprint for creating employees
# Each employee object we create is instance of class
# Here self refers to the instance of each employee

class Employee:
    # Intilalizing the class attributes.
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"

# we are creating a new method inside the class. When we say method-->its function assoicated with class
    def fullname(self):
        return f'{self.first_name} {self.last_name}'


# Both of this are employee objects and both have unique location in memory
# When we call this class method here self is instance is passed automatically when we say emp_1 = Employee()
# So we only need to provide other paramaters
# When we create emp_1 instance will be passed to main method self and each value will be passed
emp_1 = Employee('Test1', 'User', 5000)
emp_2 = Employee('Test2', 'User', 6000)

print(emp_1)
print(emp_2)

print(emp_1.first_name)
print(emp_1.email)

# This method we have already defined in class and when we call this method fullname here it gets output here
# We need fullname() paranthesis here because this is method and not an attribute
# When I call instance with method self calls automatically and I dont have to pass it
print(emp_2.fullname())
print(emp_1.fullname())

# This prints the same as when we call emp_1.fullname()
# When I call class with method I have to manually pass the instance here. So whenever we define self inside mthod
# We are automatically passing the instance to that method
print(Employee.fullname(emp_1))
