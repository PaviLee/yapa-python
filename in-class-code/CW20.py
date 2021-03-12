class Employee:

    def __init__(self, name, pay, email):
        self.name = name
        self.pay = pay
        self.email = email
        self.prepare_the_employee();

    def prepare_the_employee(self):
        # Complicated code involving preparing the object for use
        print("The employee " + self.name + " is now prepared!")


# Created two employees
emp_1 = Employee("Jim Davis", 4000, "jim_davis@gmail.com")
emp_2 = Employee("Bob Wilson", 50, "bob_wilson@gmail.com")

# emp_1.name = "Jim Davis"
# emp_1.pay = 4000
# emp_1.email = "jim_davis@gmail.com"
#
# emp_2.name = "Bob Wilson"
# # I forgot to give emp_2 a pay
# emp_2.email = "bob_wilson@gmail.com"

print(emp_1.name)
print(emp_1.pay)
print(emp_1.email)

print(emp_2.name)
print(emp_2.pay)
print(emp_2.email)
