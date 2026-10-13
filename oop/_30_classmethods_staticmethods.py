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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):  # as alternative constructor
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Shashank", "Garg", 120000)
emp_2 = Employee("Srishti", "Garg", 140000)
emp_3 = Employee("Tarun", "Garg", 100000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(
    1.06
)  # can also be called using an instance of the class, works the same

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Ben-Foakes-90000"

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime

my_date = datetime.date(2026, 6, 4)
print(Employee.is_workday(my_date))
