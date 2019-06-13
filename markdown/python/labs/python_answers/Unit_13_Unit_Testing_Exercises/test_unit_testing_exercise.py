"""
title: test_unit_testing_exercise
author: eam3kzn
date: 8/10/18 9:37 AM
"""

import unittest


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


class PrimeTests(unittest.TestCase):

    def test_prime(self):
        self.assertTrue(is_prime(500))


if __name__ == '__main__':
    unittest.main()


# # Age Calculator follow-along
# def age_calculator(current_year, birth_year):
#     # Returns the age of a person
#     age = current_year - birth_year
#     if age < 0:  # If age is not a positive number, do not return the age
#         print("Not a correct age!")
#     else:
#         return age
#
#
# if __name__ == '__main__':
#     print(age_calculator(2018, 1995))