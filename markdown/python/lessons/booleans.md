---
title: "booleans"
type: "lesson"
---

# Booleans

- It is raining - True
    
- 5 is greater than 8 - False
    
- Orange Method is the best - True
    

Booleans are used to make comparisons and to control the flow of a program. Named for George Boole, the word Boolean always begins with a capitalized B. The values `True` and `False` will also always be with a capital T and F respectively, as they are special values in Python.

You can create variables and set them to either `True` or `False`

```python
is_tired = False
is_available = True
```
You can also cast a boolean values to an `integer`. `0` represents `False` and `1` represents `True`.

```python
print(int(True))
print(int(False))
```
Output:

```
1
0
```

## Comparison Operators

In programming, comparison operators are used to compare values and evaluate done to a single Boolean value of either True or False.

The table below shows Boolean comparison operators.

| Operator | What it means |
| --- | --- |
| `==` | Equal to |
| `!=` | Not Equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

To understand how these operators work, let's assign two integers to two variables in a Python program:

```python
x = 5
y = 8
```

We know that in this example, since `x` has the value of `5`, it is less than `y` which has the value `8`.

Using those two variables, we will show the above operators being used.
```python
x = 5
y = 8

print("x == y:", x == y)
print("x != y:", x != y)
print("x < y:", x < y)
print("x > y:", x > y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)
```
Output:
```
x == y: False
x != y: True
x < y: True
x > y: False
x <= y: True
x >= y: False
```

Following mathematical logic, in each of the expressions above, Python has evaluated:

- Is 5 (x) equal to 8 (y)? **False**
    
- Is 5 not equal to 8? **True**
    
- Is 5 less than 8? **True**
    
- Is 5 greater than 8? **False**
    
- Is 5 less than or equal to 8? **True**
    
- Is 5 not less than or equal to 8? **False**
    

All of these comparators can work with floating point values and strings as well. Strings are case-sensitive unless you use an additional string method.
```python
name1 = "Sally"
name2 = "sally"
print("Sally == sally: ", name1 == name2)
```
Output: `Sally == sally: False`

**Note:** There is a difference between the two operators `=` and `==`.

- `x = y` sets (changes) the value of x to be equal to y
    
- `x == y` asks if the value of x equals the value of y. No values are changed.
    

## Logical Operators

There are three logical operators that are used to compare values. These operators are `and`, `or`, and `not`.

| Operator | What it means | What it looks like |
| --- | --- | --- |
| and | True if both are true | `x and y` |
| or | True if at least one is true | `x or y` |
| not | True only if false | `not x` |

**`and` example**

To join the local basketball team, you must be at least 4 foot tall **and** at least 16 years old. Here are all the ways you would **not** be able to join the team:

- If you were at least 4 foot tall, but not at least 16 years old
    
- If you were less than 4 foot and at least 16 years old
    
- If you were less than 4 foot and less than 16 years old
    

The only way you would be able to join the team would be if you were both taller than 4 foot **and** at least 16 years old.

**`or` example**

Say they were not able to find enough people who fulfilled both requirements for the basketball team, so they made it to where you just have to meet one or more of the requirements. Now to join the local basketball team, you must be at least 4 foot tall **or** at least 16 years old. Here are now all of the ways you **can** join the team:

- If you were at least 4 foot tall, but not at least 16 years old
    
- If you were less than 4 foot and at least 16 years old
    
- If you were at least 4 foot tall, and at least 16 years old
    

The only way you would be able to not join the team if you were neither taller than 4 foot or at least 16 years old.

Example Uses of and, or and not
```python
print((9 > 7) and (2 < 4))  # Both expressions are True
print((8 == 8) or (6 != 6)) # One expression is True
print(not(3 < = 1))          # The expression is True
```
Output:
```
True
True
True
```
In the first case:

`print((9 > 7) and (2 < 4))`

**Both** `9 > 7` and `2 < 4` needed to evaluate to True since the and operator was being used.

In the second case:
```python
print((8 == 8) or (6 != 6))
```
Since `8 == 8` evaluated to True, it did not make a difference that `6 != 6` evaluates to False because the or operator was used. If we had used the and operator, this would evaluate to False.

In the third case:
```python
print(not(3 < = 1))
```
The **not** operator negates the False value that `3 <= 1` returns.
