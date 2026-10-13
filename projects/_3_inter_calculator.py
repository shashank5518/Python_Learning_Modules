import logging
from contextlib import contextmanager
import os

os.chdir("D:/Python/projects/")


class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot Divide by Zero !!")
        return num1 / num2

    def exp(self, num1, num2):
        return num1**num2

    def floor(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot Divide by Zero !!")
        return num1 // num2

    def rem(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot Divide by Zero !!")
        return num1 % num2


logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(message)s",
)


@contextmanager
def calc_logger(expression):
    logging.info(f"Starting Calculation: {expression}")

    def log_result(result):
        logging.info(f"Result: {result}")

    try:
        yield log_result
    except Exception:
        logging.exception(f"Calculation Failed: {expression}")
        raise
    else:
        logging.info(f"Calculation Completed: {expression}")
    finally:
        logging.info(f"{expression} was logged \n")


operations = {
    "+": Calculator.add,
    "-": Calculator.sub,
    "*": Calculator.mul,
    "/": Calculator.div,
    "//": Calculator.floor,
    "%": Calculator.rem,
    "**": Calculator.exp,
}
a = float(input("Enter first num: "))
operator = input("Enter operator: ")
b = float(input("Enter second number: "))

if operator not in operations:
    raise ValueError("Invalid Operator")

expression = f"{a} {operator} {b}"

with calc_logger(expression) as log:
    calc = Calculator()
    result = operations[operator](calc, a, b)
    log(result)

print(result)
