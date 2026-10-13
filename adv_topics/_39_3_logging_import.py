import os

os.chdir("D:/Python/adv_topics/")

import logging

# import _39_1_logging_advanced

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("_39_4_test_log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# logging.basicConfig(filename='_39_4_test_log', level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error('Tried Dividing By Zero')
        logger.exception("Tried Dividing By Zero")
    else:
        return x / y


num_1 = 20
num_2 = 0

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
logger.debug(f"Addition: {num_1} + {num_2} = {add_result}")

sub_result = subtract(num_1, num_2)
logger.debug(f"Subtraction: {num_1} - {num_2} = {sub_result}")

mul_result = multiply(num_1, num_2)
logger.debug(f"Multiplication: {num_1} * {num_2} = {mul_result}")

div_result = divide(num_1, num_2)
logger.debug(f"Division: {num_1} / {num_2} = {div_result}")
