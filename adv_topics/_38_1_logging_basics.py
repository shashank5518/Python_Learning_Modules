import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(
    filename="adv_topics/_38_2_test_log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


num_1 = 20
num_2 = 10

# add_result = add(num_1, num_2)
# print(f"{num_1} + {num_2} = {add_result}")

# sub_result = subtract(num_1, num_2)
# print(f"{num_1} - {num_2} = {sub_result}")

# mul_result = multiply(num_1, num_2)
# print(f"{num_1} * {num_2} = {mul_result}")

# div_result = divide(num_1, num_2)
# print(f"{num_1} / {num_2} = {(int)(div_result)}")

# add_result = add(num_1, num_2)
# logging.warning(f"Addition: {num_1} + {num_2} = {add_result}")

# sub_result = subtract(num_1, num_2)
# logging.warning(f"Subtraction: {num_1} - {num_2} = {sub_result}")

# mul_result = multiply(num_1, num_2)
# logging.warning(f"Multiplication: {num_1} * {num_2} = {mul_result}")

# div_result = divide(num_1, num_2)
# logging.warning(f"Division: {num_1} / {num_2} = {(int)(div_result)}")

add_result = add(num_1, num_2)
logging.debug(f"Addition: {num_1} + {num_2} = {add_result}")

sub_result = subtract(num_1, num_2)
logging.debug(f"Subtraction: {num_1} - {num_2} = {sub_result}")

mul_result = multiply(num_1, num_2)
logging.debug(f"Multiplication: {num_1} * {num_2} = {mul_result}")

div_result = divide(num_1, num_2)
logging.debug(f"Division: {num_1} / {num_2} = {(int)(div_result)}")
