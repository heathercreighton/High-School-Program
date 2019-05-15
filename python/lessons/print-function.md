---
title: "print-function"
type: "lesson"
---
Create a new Python file in your project called `print_practice`. Type the following on the first line of this file:
```python
print("Hello world!")
```
Right-click anywhere in the text portion of PyCharm and press `run` to run this program.

Let's discuss what we're putting within the parenthesis of the print function. It is a data-type called a **string**. The important thing to note right now about strings, is that they require `"` quotation marks around them so that the function knows we're handing it a string.

## `print()` Set Up

`print`'s displaying whatever you put within the parenthesis in your console (the bottom of PyCharm) once the program is run.

In previous versions of Python the print function was actually a "print statement" and was written like so:
```python
print("Hello world!")
```
In Python3, it is now a print **function** and the syntax has changed to be written with parenthesis at all times, as you would to call any function:

print()
Keep these important words in mind: **Data-Type**, **String** and **Function**. We'll be talking much more about all of these as we dig deeper into our "Hello world!" program.

### New Line and Tabbed Characters

We can format our output of `print()` functions by including a few characters within our string.

To create a new line in the output, type `\n` such as:

print("Hello,\nwelcome to Orange Method!")
If we want to tab over to create more space between items within our string, we can use `\t` like so:
```python
print("Testing, testing\t1\t2\t3...")
```
We can combine the two to make cool, interesting and useless patterns in our output.

Copy and paste the following into the Python Console:
```python
print("Testing, testing\n\t1\n\t\t2\n\t\t\t3...")
```

## Multi-line Printing

You may use the `end=" "` keyword in Python3 to be able to print out content on one line while using several different `print()` function statements.

For example, if you just print out:
```python
print("Hello,")
print("my name is")
print("George")
```
The above will print out on three separate lines. In order to get it to print on one line as a sentence, do the following with the `end=" "` keyword:
```python
print("Hello,", end=" ")
print("my name is", end=" ")
print("George")
```