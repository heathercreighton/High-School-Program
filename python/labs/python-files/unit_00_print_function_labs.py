"""
filename: print_function_labs.py
author: Elizabeth Phillips
date: May 8th, 2018
description: All of the labs for print functions
"""

import random
# link:print-function-labs.html#multiple_print_statements
'''Multiple Print Statements'''
print("Elizabeth", end=", ")
print("Emily", end=", ")
print("Bob", end=", ")
print("Antonio")

# link:print-function-labs.html#ascii_art
'''ASCII Art'''
print("###############")
print("###############")
print("####")
print("####")
print("########")
print("########")
print("####")
print("####")
print("###############")
print("###############")

# link:print-function-labs.html#random_salary
'''Random Salary'''
import random

# Random salary exercise
name = input("Enter your name: ")
salary = int(input("Enter your salary: "))

raise_per = (random.randint(0, 100))
raise_amount = salary + ((raise_per / 100) * salary)

print(f"{name}, your current salary is {salary} quid.")
print(f"Your raise is {raise_per}% of {salary}")
print(name + ", your new salary is " + str(raise_amount) + " quid.") # Example of concatenation with + instead of string formatting with f
