import unittest


def ageCalculator(current_year, birth_year):
    # Returns the age of a person
    age = current_year - birth_year
    if age < 0:  # If age is not a positive number, do not return the age
        print("Not a correct age!")
    else:
        return age

class AgeTestCase(unittest.TestCase):

    def testAge(self):
        self.assertTrue(ageCalculator(2018, 1990))


if __name__ == '__main__':
    unittest.main()
