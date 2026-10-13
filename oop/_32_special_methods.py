# __init__ is a special method


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

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Shashank", "Garg", 120000)
emp_2 = Employee("Srishti", "Garg", 140000)
emp_3 = Employee("Tarun", "Garg", 100000)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())

print(int.__add__(1, 2))
print(str.__add__("a", "ba"))

print(emp_1 + emp_2)

print(len("test"))
print("test".__len__())

print(len(emp_1))
