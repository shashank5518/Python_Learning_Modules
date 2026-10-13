class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@company.com"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}".title()

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first_name = first
        self.last_name = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first_name = None
        self.last_name = None


emp_1 = Employee("John", "Smith")

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first_name = "Jim"
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = "Shashank Garg"
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)
