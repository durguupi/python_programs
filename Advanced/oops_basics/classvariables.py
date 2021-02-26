#  how to differentiate between a Class variable and instance variable
# Class variables are variables that we set inside a class, and are shared among all instances.
# here the number of total employs should be the same to every employ, no matter which employee we are referring to.
# Therefore,emp_1.num_of_employ = emp_2.num_of_employ = Employee.num_of_employ

class Employee:

    raise_amount = 1.05
    num_of_employs = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + ".example.com"

        Employee.num_of_employs += 1

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

# Instance variables are variables that are different from each instance. For example, the names and the pay for each employee.
# They have to be different.

    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount


print(
    f"Before creating the instance of employee class num0femploys: {Employee.num_of_employs}")
emp_1 = Employee('Test1', 'User1', '5000')
emp_2 = Employee('Test2', 'User2', '6000')

print(emp_1.fullname())
print(emp_2.fullname())
print(emp_1.email)


# First python checks if a variable is found within an instance if it is then it takes that variable
# Here its present so the value 1.08 is taken and rolloutpay is calculated
emp_2.raise_amount = 1.08
print(emp_2.raise_amount)
emp_2.apply_raise()
print(emp_2.pay)

# if not found within the instance and programmers try to access the variable, python automatically looks in
# in the variable of the instance's class, and then the more classes that the instance's class inherits from.
# Here emp_1 doesnt have variable of raise_amount but the Employee class has that so the emp_1 instance takes the
# value from the class Employee which is 1.05 and calcluates the rollout pay.
print(emp_1.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)


# With the help of dict method we can find the namespace present inside the class and instance of that class
print(Employee.__dict__)
print(emp_1.__dict__)
# Now since we have defined raise_amount for emp_2. This variable takes precedence when we calculate the rolloutpay
# And the same can be seen using dict method wehere we have variable for raise-amount
print(emp_2.__dict__)
print(
    f"After creating the instance of employee class num0femploys: {Employee.num_of_employs}")
print(emp_1.num_of_employs)
print(emp_2.num_of_employs)
