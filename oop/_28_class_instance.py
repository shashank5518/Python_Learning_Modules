class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"

    def fullname(self):
        return f"{self.first_name} {self.last_name}".title()


emp_1 = Employee("Shashank", "Garg", "$120000")
emp_2 = Employee("Vinay", "Ghosh", "$80000")
emp_3 = Employee("Champak", "Chacha", "$100000")

print(emp_1.first_name)
print(emp_1.last_name)
print(emp_1.email)
print(emp_1.pay)
print()
print(emp_2.first_name)
print(emp_2.last_name)
print(emp_2.email)
print(emp_2.pay)
print()
print(emp_1.fullname())
print(emp_2.fullname())
print(emp_3.fullname())
print()
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
print(Employee.fullname(emp_3))
