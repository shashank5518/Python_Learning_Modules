import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("adv_topics/_39_2_employee_log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logging.basicConfig(filename = 'adv_topics/_39_2_employee_log', level = logging.INFO, format = '%(levelname)s:%(name)s:%(message)s')


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}".title()


emp_1 = Employee("John", "Doe")
emp_1 = Employee("Jane", "Mary")
emp_1 = Employee("Peter", "Pewterschmidt")
