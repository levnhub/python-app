import time
import datetime as d
import sys
import os
import platform
from math import sqrt as s, ceil
import module_my as my
from module_my import add_three_numbers as add

# Modules

time.sleep(1)  # seconds

print("Hello")

print(d.datetime.now().date())

print("Path:", sys.path)
print("OS: ", os.name)
print("Platform: ", platform.system())

print("Square", ceil(s(100)))

# My module

print(my.name)
my.Hello()
print(add(5, 3, 6))
print(add(5, 3, 0))
