import os

os.chdir("D:/Python/testing")


class Employee:
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.first = fname
        self.last = lname
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}".title()

    def apply_raise(self):
        self.pay = (int)(self.pay * self.raise_amount)  # or Employee.raise_amount
