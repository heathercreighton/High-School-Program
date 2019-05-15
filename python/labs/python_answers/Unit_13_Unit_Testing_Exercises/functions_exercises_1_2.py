"""
title: functions_exercises_1_2
author: eam3kzn
date: 6/11/18 2:45 PM
"""


# Benefits of code follow along
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return f"{benefit} is a benefit of functions!"


def the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


# Age Calculator follow-along
def age_calculator(current_year, birth_year):
    # Returns the age of a person
    age = current_year - birth_year
    return age


# Averaging Numbers follow-along
def average_numbers(a, b, c):
    d = (a + b + c) / 3
    return d


if __name__ == '__main__':
    print(age_calculator(2018, 1900))
    print(average_numbers(4, 7, 8))
    the_benefits_of_functions()
