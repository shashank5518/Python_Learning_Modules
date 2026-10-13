import logging

logging.basicConfig(
    filename="adv_topics/_38_4_employee_log",
    level=logging.INFO,
    format="%(levelname)s:%(message)s",
)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}".title()


emp_1 = Employee("John", "Doe")
emp_1 = Employee("Jane", "Mary")
emp_1 = Employee("Peter", "Pewterschmidt")
