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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        # Employee.__init__(self, fname, lname, pay) # same as above
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for employee in self.employees:
            print(f"--> {employee.fullname()}")


dev_1 = Developer("Shashank", "Garg", 120000, "Python")
dev_2 = Developer("Guddi", "Garg", 110000, "Java")
mgr_1 = Manager("Srishti", "Garg", 140000, [dev_1])

print(dev_1.email)
print(mgr_1.email)
print(dev_1.prog_lang)

# print(Developer.__dict__)
# print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1.print_emps()
print()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
print()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# isinstance( , )
# issubclass( , )
