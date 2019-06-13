---
title: "conditional-statements"
type: "lesson"
---

# Conditional Statements

- If I have enough money in the bank, I will go to a fancy dinner tonight. If not, I will eat at home.
    
- If I do the correct secret hand shake at the door, I can get in the secret club. If not, I will go home.
    
- If it is not raining outside, I will go for a run. If it is, I will stay home.
    

There are cases when working on a program we want certain parts of a program to execute, but only if a certain conditions are met. With conditional statements, we can have code that sometimes runs and at other times does not run, depending on the conditions of the program at that time. By using conditional statements, program can determine whether certain conditions are being met and then be told what to do next.

## If Statements

An `if` statement helps with deciding whether a statement is true or false, and run code only in the case that the statement is true.

**If Statement Set Up**
```
if condition is true:
  [do something]
```
Notice that the `[do something]` section is **indented**. In conditional statements, the indentation tells the Python Interpreter which line(s) of code are executed if a statement is correct.

Checking if someone guessed the correct number
```python
secret_num = 10
guess = int(input("Enter a secret number: "))
if guess == secret_num:
  print("Yay! You won!")
```
With this code, we have the variable `secret_num` and are giving it the integer value of 10. A second variable called `guess` is created and is set to the value of an integer that the user types in. The `if` statement is used to check if the variable `guess` equals `secret_num`. If the user did guess the correct number, the program would print out `Yay! You won!`. If the user did not guess the correct number, nothing would be printed.

Example of the user guessing correctly
```
Enter a secret number: 10
Yay! You won!
```
In the above example, the user typed in 10, which is equivalent to the secret number. Because the values were equivalent, the code executed the print statement.

Example of the user guessing incorrectly
```
Enter a secret number: 255
```
One common action for a person to do is to check to see if you have nay money in your bank account. If you have a negative amount (any amount less than zero), you should receive a warning of some kind. This could be done with the following code:
```python
balance = 100
if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")
```
The above code would not have any output because the balance is 100, which is greater than zero!

If the above code was changed to:
```python
balance = -5
if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")
```
The above code would output `Balance is negative. Put funds in your account or you will be charged a penalty.` because the balance is -5, which is less than zero!

## Else Statements

An `if` statement by itself will only handle if the condition is True. It is very common that you would want to give a response if the condition is true **or** it is false. In the bank example, we might also want to give a response if the user has a balance in their account. This can be done with an `else` statement. An `else` statement is the "otherwise" statement, taking care of if the original `if` condition is false.

**`else` Statement Set Up**
```
if condition1:
  [do 1st option]
else:
  [do 2nd option]
```
```python
balance = 25
if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")
else:
  print("Balance is positive.")
```
The output is `Balance is positive` because the balance is still 25, which is above zero.

If the above output was changed:
```python
balance = -33
if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")
else:
  print("Balance is positive.")
```
The output is `Balance is negative. Put funds in your account or you will be charged a penalty.` because the balance is -33, which is below zero.

## Else If Statements

So far, we have only checked to see if one condition is True or False. Usually a program has many different conditions to consider. To consider other conditions, you use an **else if** statement, which in Python is written as `elif`. The `elif` looks like the `if` statement and will evaluate another condition.

**elif Set Up**
```
if condition1:
  [do 1st option]
elif condition2:
  [do 2nd option]
else:
  [do 3rd option]
```
Back to the bank account example, we may want to consider three possible situations:

* If the Balance is negative. Put funds in your account or you will be charged a penalty.
* If the balance is equal to zero
* If the balance is positive

In Python, this would be written as:
```python
if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")
elif balance == 0:
  print("Balance is equal to zero, add funds soon.")
else:
  print("Balance is positive.")
```
There are three possible outputs can now occur:

- If the variable `balance` is equal to 0, we will receive the output from the `elif` statement (`Balance is equal to zero, add funds soon.`)
    
- If the variable `balance` is set to a positive number, we will receive the output from the `else` statement (`Balance is positive.`)
    
- If the variable `balance` is set to a negative number we will receive the output from the `if` statement (`Balance is negative. Put funds in your account or you will be charged a penalty`)
    

You can have multiple `elif` statements in the same group, allowing for a program to choose between 2+ conditions. For example, with the Orange Method classes, based on your knowledge of particular topics you can take specific courses. It would be helpful to know based on certain requirements what classes you qualify for. Different qualifiers include knowledge in Git and Python. Each of these abilities can be rated on a 1 to 3 scale, 1 representing "No knowledge at all" and 3 representing "Expert". It would be helpful to be able to type in your abilities and see what courses are appropriate for you.
```python
if git_skill == 1 and python_skill == 1:
  print("Start off with Git Foundation")
elif git_skill >= 2 and python_skill == 1:
  print("Start off with Python Foundation")
elif git_skill == 2 and python_skill == 2:
  print("Start off with either Python Pillars or Git Pillars")
elif git_skill == 3 and python_skill == 2:
  print("Start off with Python Capstone")
else:
  print("Git Capstone or Python Capstone")
```
There are five paths defined in the above example.

- If the user has the `git_skill` level of a 1 and a `python_skill` level of a 1, we will receive the output from the `if` statement. (`Start off with Git Foundation`)
    
- If the user has the `git_skill` level of a 2 or higher and a `python_skill` level of a 1, we will receive the output from the first `elif` statement. (`Start off with the Python Foundation`)
    
- If the user has the `git_skill` level of a 2 and a `python_skill` level of a 2, we will receive the output from the second `elif` statement. (`Start off with either Python Pillars or Git Pillars`)
    
- If the user has the `git_skill` level of a 3 and a `python_skill` level of a 2, we will receive the output from the third `elif` statement. (`Start off with the Python Capstone`)
    
- If the user has any other combination (like a `git_skill` level of 3 and `python_skill` level of 3), we will receive the output from the `else` statement. (`Git Capstone or Python Capstone`)
    

# main

Although in Python you can call the function at the bottom of your program and it will run (as we have done in the examples above), many programming languages (like C++ and Java) require a `main` function in order to execute. Including a `main()` function, though not required, can structure our Python programs in a logical way that puts the most important components of the program into one function. It can also make our programs easier for non-Python programmers to read.

We'll start with adding a `main()` function to the `hello()` example. We will include a `print` in the `main()` to let us know that we're in the `main()` function. Additionally, let's call the `hello()` function within the `main()` function.
```python
def hello():
    print("Hello, World!")

def main():
    print("This is the main function")
    hello()

main()
```
Output:
```
This is the main function.
Hello, world!
```
Because we called the `hello()` function within `main()` and then only called `main()` to run, the `Hello, World!` text printed only once, after the string that told us we were in the main function.

Next we're going to be working with multiple functions, so it is worth reviewing the variable scope of global and local variables. If you define a variable within a function block, you'll only be able to use that variable within that function. If you would like to use variables across functions it may be better to declare a global variable.

In Python, `'main'` is the name of the scope where top-level code will execute. When a program is run from standard input, a script, or from an interactive prompt, its `name` is set equal to `'main'`.

Because of this, these is a convention to use the following construction:
```python
if __name__ == '__main__':
  # Code to run when this is the main program here
```
This lets program files be used either:

- as the main program and run what follows the `if` statement
    
- as a module and not run what follows the `if` statement
    

Let's expand on our program above. In this program we'll declare a global variable and modify our original `names()` function so that the instructions are in two discrete functions.

The first function, `has _vowel()` will check to see if the name string contains a vowel.

The second function `print _letters()` will print each letter of the `name` string.

```python
#Declare global variable `name` for use in all functions
name = input('Enter your name: ')

# Define function to check if name contains a vowel
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')

# Iterate over letters in name string
def print_letters():
    for letter in name:
        print(letter)

# Define main method that calls other functions
def main():
    has_vowel()
    print_letters()

# Execute main() function
if __name__ == '__main__':
    main()
```
The output from this file will only occur if the current file is the main file being run.
