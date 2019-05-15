---
title: "unit-tests"
type: "lesson"
---
TDD exists to improve the quality and the design of our code.

**What is a "unit"?**

The unit in "unit testing" is the function that we're testing against. If we're trying to figure out if a number is odd, we'll write this function to make sure our unit returns appropriately for odd numbers only.

**What are "tests"?**

The tests test against the unit. We'll test the unit function we wrote by calling the `unittest` module in Python, and telling it to "assert **true**" if something in our unit is true, or "assert **false**" if something in our unit is false.

Python will spit out an easily readable message depending on if the test finds our unit to be `True` or `False` in this case.

## Using the `unittest` module

Let's see what a **unit** and **tests** look like as a whole:
```python
import unittest

# Here's our "unit" checking that n is an odd number
def is_odd(n):
    return n % 2 == 1

# Here's our "unit test" class
class IsOddTests(unittest.TestCase):

    # First function takes the IsOdd function and use the parameter n=1 as true,
    # otherwise fail the test.
    def test_one(self):
        self.assertTrue(is_odd(1))

    # Second function takes IsOdd function and use the parameter n=2
    # as automatic fail of test.
    def test_two(self):
        self.assertFalse(is_odd(2))

if __name__ == '__main__':
  unittest.main()
```
Different assert statements**

| Method | Checks That |
| --- | --- |
| assertEqual(a, b) | `a == b` |
| assertNotEqual(a, b) | `a != b` |
| assertTrue(x) | `bool(x) is True` |
| assertFalse(x) | `bool(x) is False` |
| assertIs(a, b) | `a is b` |
| assertIsNot(a, b) | `a is not b` |
| assertIsNone(x) | `x is None` |
| assertIsNotNone(x) | `x is not None` |
| assertIn(a, b) | `a in b` |
| assertNotIn(a, b) | `a not in b` |
| assertIsInstance(a, b) | `isinstance(a, b)` |
| assertNotIsInstance(a, b) | `not isinstance(a, b)` |

### Class? Wut?

We have only mentioned **classes** in this course, but we can briefly explain them here. A class is used in this situation in order to run both "test cases" - `test_one()` and `test_two()`.

When you're writing a method (or function) for a test, there are a few rules:

1. The name of the function should start with the word `test` like `test_one()` and `test_two()` in the above example.
    
2. They both must have the argument `(self)` as well.
    
3. They have to be within a **class** whose argument must be `(unittest.TestCase)`
    

Technically `IsOddTests` is called a Test Fixture, even though `TestCase` is a class that it's derived from. As a class itself, it's derived from `unittest.TestCase`, and **Test Fixtures group related test cases together**.

It's important to note that you wouldn't usually write your tests in the same file as your unit that's being tested. This is just for instructional purposes. You can also begin writing tests this way, but extract the code or tests later to organize your codebase properly.

## Start with tests

Being test infected is a **good** thing! This means that you must write a program by first writing unit test. That's right - don't write the code first, write the tests first.

**First step in testing is to create an empty test fixture that fails:**
```python
import unittest

class FooTests(unittest.TestCase):

    def test_foo(self):
        self.assertTrue(False)

if __name__ == '__main__':
  unittest.main()
```
Output should look something like this:

![test fail](img/test/test-fail.png)

You may be asking…​ **but I don't even know what I'm testing yet!**

That's the point. You don't have to. If you start with these bones to test before you even start writing code, you'll be able to code to the tests instead of testing against old, buggy code.

Before we specify what code (unit) we want to test, let's define what exactly a `unit` can consist of. It can be an entire module, a single function or even just a measley `if/else` statement. You just have to ensure that the code you're testing is isolated from any other code in your codebase.

##Example: Prime number testing

Say we'd like to figure out if a number is a `prime` number. **Prime Number: A whole number, greater than 1, that cannot be formed by multiplying two smaller whole numbers**

We'll first take our test example from above, and we'll change the name of the class to something relevant like `PrimeTestCase` and the function name to `test_prime()`
```python
import unittest

class PrimeTestCase(unittest.TestCase):

    def test_prime(self):
        self.assertTrue(False)

if __name__ == '__main__':
  unittest.main()
```
Now, to add the unit to our test:
```python
import unittest

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

class PrimeTestCase(unittest.TestCase):

    def test_prime(self):
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
  # Call the unittest module on main() function which will run the entire program
  unittest.main()
```
The output should be that the test is `OK` which means that we wrote our **unit** properly. Since we know 5 is a prime number already, we use it as the argument within the test case. This proves that our function to find prime numbers was written correctly.

In order to make sure it's just not checking for the number 5, write more assertions with various numbers to test. Observe the output after running the file.
