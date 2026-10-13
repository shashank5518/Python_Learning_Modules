class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.first = fname
        self.last = lname
        self.email = f"{fname.lower()}.{lname.lower()}@company.com"
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}".title()

    def apply_raise(self):
        self.pay = (int)(self.pay * self.raise_amount)  # or Employee.raise_amount


emp_1 = Employee("Shashank", "Garg", 120000)
emp_2 = Employee("Srishti", "Garg", 140000)
emp_3 = Employee("Tarun", "Garg", 100000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.05
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount = 2.00
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print()
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)

print(Employee.num_of_employees)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# instance variable is checked before class variable, use emp.__dict__ and Employee.__dict__ to understand
