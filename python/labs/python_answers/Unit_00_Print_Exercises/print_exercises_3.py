"""
title: print_exercises_3
author: eam3kzn
date: 6/11/18 1:09 PM
"""

import random

# Random salary exercise
name = input("Enter your name: ")
salary = int(input("Enter your salary: "))

raise_per = (random.randint(0, 100))
raise_amount = salary + ((raise_per / 100) * salary)
raise_amount = str(raise_amount)

print(f"{name}, your current salary is {salary} quid.")
print(f"Your raise is {raise_per}% of {salary}")
print(f"{name}, your new salary is {raise_amount} quid, mate.")
