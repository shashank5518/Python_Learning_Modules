class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"({self.name}, {self.age}, ${self.salary})"


e1 = Employee("Carl", 34, 70000)
e2 = Employee("John", 27, 90000)
e3 = Employee("Kumar", 32, 80000)

employees = [e1, e2, e3]
# print(employees)
from operator import attrgetter

# s_employees = sorted(employees, key=lambda e: e.age, reverse=True)
s_employees = sorted(employees, key=attrgetter("name"))
print(s_employees)
