---
title: "exceptions"
type: "lesson"
---
## SyntaxError

In order to evaluate an error, we'll write a `try` and `except` statement. `try` means we're telling Python to try to evaluate the following line.

Using the `eval` keyword, we'll attempt to evaluate an expression. This will raise a syntax error since Python is expecting `eval` to take a valid expression. There is no `===` operator in Python.

After `except` we'll print out the string "You cannot do that" to gracefully tell the user that they're doing something that causes Python to error.

```python
try:
    eval('x === x')
except SyntaxError:
    print("You cannot do that")

```
Output: `You cannot do that`

The output is not descriptive enough. We don't fully understand why we're running into the exception in this instance. It's important to understand what the error is and even what we might need to correct to fix it.

Beware of using try/catch to evaluate some syntax errors. Python will catch a syntax error before your file is executed. The parser doesn't see that there is an `except` statement at all and expects you to recognize and fix syntax errors before executing.

## ZeroDivisionError

```python
print(10 + (1 / 0))
```

The above evaluation will give us a ZeroDivisionError. Let's handle the ZeroDivisionError exception. Use the most specific wording which semantically fits your issue.

```python
try:
    print(10 + (1 / 0))
except ZeroDivisionError:
    print("Oops! We can't divide by zero, please choose a different number and re-evaluate.")
```
Output: `Oops! We can't divide by zero, please choose a different number and re-evaluate.`

## NameError

```python
print(4 + spam * 3)
```

A useful way of raising errors is to manually raise the actual error Python gives us, but to put it within a human readable string.

If we want to take the above example and raise (or **throw**) Python's `NameError` we can use it like so:

```python
try:
  print(4 + spam * 3)
except NameError as error:
  print('You have encountered a NameError because', error)
```
By using the variable `error` Python will know to print out the actual error semantically. You can choose to only print this error out, or concatenated it with a string like the above example.

## TypeError

```python
print("2" + 2)
```
Let's create our own TypeError using the `error` variable using the previous example as guidance.

## Multiple Exceptions

We can write an exception for more than one error at a time. Let's take the two examples above, `NameError` and `TypeError` and write one statement that handles both of them:

```python
try:
    print("2" +  spam + 15)
except (NameError, TypeError):
    print("Very sorry, we are unable to evaluate your request. Please correct errors and re-evaluate.")
```

Output: `Very sorry, we are unable to evaluate your request. Please correct errors and re-evaluate.`

It is possible to have multiple excepts for one `try` in case you want to give specific errors for each specific kind of errors.

```python
try:
    print("2" +  spam + 15)
except TypeError as e:
    print("You gave the wrong type there buddy!", e)
except NameError as e:
    print("That variable name does not exist!", e)

```
Output: `That variable name does not exist! name 'spam' is not defined`

## Raise

We can also use the keyword `raise` to raise an error in Python.

In the following example, `raise` is put within an `if` statement which is within a function that will be called within the `try` and `except` below. We're raising an error at line 3 which throws the exception we print out on line 6.

**Finally Example using raise**

```python
def divide_this(x, y):
    try:
        x / y
        raise ZeroDivisionError
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("Executing finally")

print(divide_this(10, 10))

```

**Else Example**

```python
def divide_this(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(e)
    else:
        print("Executing else", result)

print(divide_this(10, 10))
```

Common Errors


<table>
<tr><td width="15%"> <code>Exception</code> </td> <td width="35%">Base class for all exceptions </td><td width="50%">

```python
try:
  print(10 / 0)
except Exception as e:
  print("This exception was raised:", e)
```
</td></tr>
<tr><td><code>ArithmeticError</code> </td> <td>Base class for all errors that occur for a numeric calculation</td> <td>

```python
try:
  print(10 / 0)
except ArithmeticError as e:
  print("This exception was raised:", e)
```
</td></tr>
<tr><td><code>
ZeroDivisionError</code> </td> <td>
Raised when division or modulo by zero takes place for all numeric types</td> <td>

```python
try:
  print(10 / 0)
except ZeroDivisionError as e:
  print("This exception was raised:", e)
```

</td></tr>
<tr><td><code>ModuleNotFoundError</code> </td> <td>
Raised when an import statement fails </td> <td>

```python
import somestuff
try:
  print(somestuff.amethod())
except ModuleNotFoundError as e:
  print(e)
```
</td></tr>
<tr><td><code>IndexError</code> </td> <td>Raised when an index is not found in a sequence</td> <td>

```python
example_list = [1, 2, 3, 4]
try:
  print(example_list[4])
except IndexError as e:
  print(e)
```
</td></tr>
<tr><td><code>KeyError</code> </td> <td>Raised when the specified key is not found in the dictionary</td> <td>

```python
example_dictionary = {'a' : 1, 'b': 2, 'd': 4}
try:
  print(example_dictionary['c'])
except KeyError as e:
  print("You do not have key", e, "in this dictionary")
```
</td></tr>
<tr><td><code>SyntaxError</code> </td> <td>Raised when there is an error in Python syntax</td> <td>

```python
try:
  eval('x === x')
except SyntaxError as e:
  print("This exception was raised:", e)
```
</td></tr>
<tr><td><code>TypeError</code> </td> <td>Raised when an operation or function is attempted that is invalid for the specified data type
</td> <td>

```python
try:
    print("2" +  15)
except TypeError as e:
    print(e)
```
</td></tr>
</table>