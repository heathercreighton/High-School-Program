"""
title: exception_writing_exercises
author: eam3kzn
date: 6/11/18 1:38 PM
"""

# Error Writing Exercises

# Eval on a Syntax Error
try:
    eval('x === x')
except SyntaxError as e:
    print("You cannot do that:", e)

# Zero Division Error
try:
    print(10 / 0)
except ZeroDivisionError as error:
    print("Sorry:", error)

# Name Error
try:
    print(4 + spam)
except NameError as error:
    print("You've run into an error", error)

# Type Error
try:
    print(2 + "2")
except TypeError as e:
    print("You've run into an error:", e)

# Using Raise
try:
    salary = input("Enter your salary: ")
    salary = int(salary)
    if salary < 0:
        raise TypeError
except TypeError as e:
    print("Negative number!")
except ValueError as e:
    print(e)
else:
    print("Success!")
