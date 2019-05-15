---
title: "formatting-and-input"
type: "lesson"
---
We've introduced one built-in method for Python: `print()`. Another function important to strings is the `str()` method. We'll use the `str()` method when we need to convert a number to a string.

We'd like to print a string that says "I am 24 years old". Instead of just declaring a variable set to an integer and concatenating that variable **with** strings in the `print()` function, we have to do it differently, as you can see from the error you get when you try this.

Type the following into your PyDev Console to view the error:
```python
age = 49
print("Monty Python is " + age + " years old.")
```
The error literally says `TypeError: must be str, not int`. It's **telling** us that it wants a string! Not an int! How awesome is that!

We have three alternatives to fix this error.

First option is to **cast** the variable. To **cast** is to change the variable from one data type to another. When working with `print` and the `+` operator, we need to **cast** all variables to a string, like the following:
```python
print("Monty Python is " + str(age) + " years old.")
```
Second option is to use commas to combine the strings and variables of any type, like the following:
```python
print("Monty Python is", age, "years old.")
A third option is to use **formatting operators**
```
## Python3 Formatting

In Python3 we'd write this string like so:
```python
age = 24
print("I am {0} years old".format(age))
```
In this example, we're passing the variable `age` to the `format()` method and the `format()` method is looking for curly braces `{}` within our string to insert the variable's value (as a string), which we set to the integer `24`

If you run this in your PyDev console, the output should look like this:
```
I am 24 years old.
```
But what if we want to insert several different variables? Python3 has a solution for that as well:
```python
my_age = 24
moms_age = 60
dads_age = 59
sisters_age = 35
```
If we set these variables first, we can use a print statement to refer to each one in any order we choose:
```python
print("""My mom is {1} years old, and my dad is 1 year younger at {2} years old.
My sister is 11 years older than me, which makes her {3} years old
and I am only {0} years old.""".format(my_age, moms_age, dads_age, sisters_age))
```
Type the above `print()` statement into your PyDev console and press `return`

Your output should look like this:
```
My mom is 60 years old, and my dad is 1 year younger at 59 years old.
My sister is 11 years older than me, which makes her 35 years old
and I am only 24 years old.
```
Notice that we used three `"""` quotation marks around our string. This is because it's a block of text that would have been too long to fit on the screen. The triple quotations help us make line breaks without errors.

You may be wondering what the numbers within the `{}` represent, care to take a guess?

Hint: It relates to the order of the variables as they're written within the `format()` method.

Now we're getting into what's called **indexing**. The index always starts at `0` and counts up, by `1` until the end of the list. Therefore in this example, `my_age` is index `0`, `moms_age` is index `1` and so forth. The numbers within the `{}` correspond to the index of each variable. It's okay if this is confusing now, we'll go into much more detail in the following section.

**Using Variables in Print Formatting**

We can also use print formatting with the variable names. Using the example from before using variables by placing an `f` at the front of the quotes inside of the quotes.
```python
my_age = 24
moms_age = 60
dads_age = 59
sisters_age = 35

print(f"""My mom is {moms_age} years old, and my dad is 1 year younger at {dads_age} years old.
My sister is 11 years older than me, which makes her {sisters_age} years old
and I am only {dads_age} years old.""")
```

## User Input

So far, all values that we have printed out and stored in variables have been typed right there in the code. Every time we would run the a program, it would give us the exact same output. This is not representative of many programs out there, as most programs take in some kind of input that will alter what the output is. In most cases, the input will come from the keyboard. For this very purpose, Python provides the function `input()`. `input()` takes in one **argument** (value in between the parenthesis), which is the prompt for the user.

Input Example:
```python
name = input("Enter your name: ")
print("Nice to meet you " + name + "!")
```
If you were to run the above code you would get the following:
```
Enter your name: Dorothy
Nice to meet you Dorothy!
```
- `Enter your name:` is the prompt from the input function. This allows the user to know what you are wanting from them.
- `Dorothy` is what the user typed in. This value is then stored in the `name` variable.
- `Nice to meet you` and `!` are the values in the print statement that will be the same every time you run the program.
- The second `Dorothy` is using the value that was given by the user and stored in the `name` variable.