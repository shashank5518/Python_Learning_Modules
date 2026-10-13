# import _8_1_modules_std_library
# import _8_1_modules_std_library as mm
# from _8_1_modules_std_library import find_index, test
# from _8_1_modules_std_library import *
from modules_and_packages._8_1_modules_std_library import find_index as fi, test as t
import sys

courses = ["History", "Math", "Physics", "CompSci"]

index = fi(courses, "Math")
print(index)

print(t)

print(sys.path)

# sys.path.append('location path')

import random

rand_num = random.random()  # between 0 and 1
rand_int = random.randint(1, 100)
random_course = random.choice(courses)
print(rand_num)
print(rand_int)
print(random_course)

import math

rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

import os

print(os.getcwd())
print(os.__file__)
