---
title: "Variables"
type: "lesson"
---

**Assume a swallow weighs 60 grams, and one swallow is capable of carrying 1/3 of its own weight.**

A **variable** provides us with a way to label and access information. Variables are used as labels to store values in memory. Memory is allocated the moment you declare the variable.

**Declaring** a variable has a specific syntax:
```python
swallow_limit = 60 / 3
```
Once we create our variable, we can reference it and get the value we stored. This means we can write more organized code!

The variable above is called `swallow_limit` and the single `=` sign is telling the program to store the value on the right side of the equation to memory. The value we're telling it to store is the `float` equation `60 / 3`, which is `20.0`.

## Naming Conventions

Variable names cannot have spaces or start with digits/special characters. Variables **can** start with an underscore `_`, a lowercase letter as in our example `swallow_limit` or with a capital letter such as `Swallow_limit`. According to the pep8 style guide, you should have all lowercase letters.

| Variable Name | Valid? | pep8 approved? | Comments |
| --- | --- | --- | --- |
| `myName` | yes | no | This is the camelCase convention (capitalize the first letter of every word that comes after the first word). This goes against the pep8 style guide though. |
| `1name` | no | no | This variable starts with a number which is not allowed. |
| `int` | yes | no | This Python built-in function is technically allowed as a variable name, but is frowned upon. Its attempted usage may yield unexpected behavior, as the statement `int(x)` changes an object `x` to be type `int`. |
| `else` | no | no | This is an element of the basic syntax in Python (a **keyword**). Using a keyword as a variable name is a syntax error. Other common keywords are `for`, `if`, `not`, `return`, and `def`. |
| `my_name` | yes | yes | This variable name follows the rules of Python and pep8! |

Variables are **case sensitive** so if you decide to capitalize the first letter of your variable, be careful not to try to refer to it using the opposite case. It simply won't work.

Not only do variables make your code more organize, it makes it more readable by assigning meaning to values.

If we take our previous example, and we know that `swallow_limit = 60 / 3`, then we can re-write our previous equation with variables:
```python
swallow_limit = 60 / 3
swallows_per_cherry = 8 / swallow_limit
```
Type the above code into Python Console. Then type `swallows_per_cherry` and press `return`

You should get the output of `0.4`, which is the same figure we got from doing the equation in the previous section.

## Casting variables

If you wanted to know how many full grams that a swallow can hold, you would need to **cast** the variable. To **cast** is to change a variable from one type to another. In this case, we want to change our floating point number to an integer. To do this, we would do the following syntax:
```
type_you_want(variable_you_want_to_change)
```
To change the `swallow_limit` variable to an `int` you would do the following:
```python
swallow_limit = int(swallow_limit)
```
This would "chop off" the decimal, and give `swallow_limit` the new value of `20` rather than `20.0`.