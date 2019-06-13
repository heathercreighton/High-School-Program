"""
title: unit_testing
author: eam3kzn
date: 6/19/18 4:03 PM
"""

import unittest


def age_calculator(current_year, birth_year):
    # Returns the age of a person
    age = current_year - birth_year
    # if age < 0:  # If age is not a positive number, do not return the age
    #     print("Not a correct age!")
    # else:
    return age


# Here's our "unit test" class
class IsAgeCorrectTests(unittest.TestCase):

    # First function takes the IsOdd function and use the parameter n=1 as true,
    # otherwise fail the test.
    def test_one(self):
        self.assertGreater(age_calculator(2018, 1995), 0)


if __name__ == '__main__':
    unittest.main()
