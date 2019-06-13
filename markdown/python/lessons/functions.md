---
title: "functions"
type: "lesson"
---

# Functions

Functions are important because they allow us to divide code into useful blocks. We can create order and organization, make it more readable, and reuse it to prevent repetitiveness.

* * *

Function syntax in Python begins with the keyword `def` followed by the function name, parenthesis, and a colon. On the second line, we need to indent appropriately or else Python will not run the function and it will error.

Copy and paste the following function into PyCharm and run it:
```python
def subtract_total():
    total = 10000
    my_share = 20000
    print(my_share - total)
```
Hopefully nothing happened. But why isn't it running at all when it's within proper function syntax?

**Scope**: The `print()` is inside the scope of the `subtract_total()` function. Python doesn't see any code when this is executing, because it's "hidden" within the bounds of the function. Now we need to write the program so that Python can see within the function, and ultimately execute the `while` loop.

**Function block syntax**

In order to define a function for Python, we have to use the `def` keyword. As you can see, `def` will turn a different color in your IDE once you write the name of the function after this keyword. This is one indication that you've begun defining a function for Python to read.

Other syntax required for Python to be able to read a function is the function name. Function naming rules are as follows (from the [pep8 style guide](https://www.python.org/dev/peps/pep-0008/)):

- The first letter of the name of a function should be **lower case**
    
- The second word can be camelCase (also known as mixedCase), where the first letter of the second word is capitalized
    
- The second word (if there is one) could be separated by an **underscore** `_` as an alternative to using camelCase
    
---
The key to naming your functions is similar to naming variables. You want to be **consistent** throughout your program. If you've started naming functions in camelCase, continue to do so for all functions. This helps with code clarity, readability and the ability for others to contribute in an organized way.

---

Once you name the function properly after the `def` keyword, it is essential to put a colon `:` before writing the rest of your function.
```python
def subtract_total():
```
The rest is **all** about indentation! Python is very opinionated about indentation and it will not read a program without proper indentation. Once you've defined your function, make sure the very next line is indented, like in the `subtract_total()` example.

If you're unsure about indentation at first, that's okay. PyCharm will tell you if you've missed an indentation.

### Calling functions

In order to get a function to execute, we have to explicitly call it. Using the example above, we simply have to put the function name on the last line **outside** of the **scope** of the function.
```python
def subtract_total():
    total = 10000
    my_share = 20000
    print(my_share - total)
subtract_total()
```
Pay close attention to the lack of indentation of `def` and of the last line `subtract_total()` \- they're on the same indentation level because they're both in the same scope. Python runs line-by-line, first skipping over the `def` function, and then hitting the last line where we're explicitly instructing Python to run the `subtract_total()` function. Then, it goes back and checks to see if there are any functions, defined by `def`, called `subtract_total()`. It finally finds our function and executes the mathematical operation!

## Parameters

A **parameter** is placed within the parenthesis of a function. Parameters are declared when the function is defined as placeholders for actual objects that will be passed when the function will be called. In Python you do not declare the type of a parameter. 

Code along: Write a function called `hello()`, and put the parameter `name` within the parenthesis.
```python
def hello(name):
```
We want this function to print out `Hello your-name!`, so we need to concatenate the string "Hello" with **your** name (also a string). So we'll take the parameter `name` and use it as a variable within the `print()` function.
```python
def hello(name):
    print("Hello " + name)
hello()
```
If we run this, Python will throw a Type Error saying that `hello()` takes exactly 1 argument. When we called the function on the last line, we didn't give `hello()` any arguments!

Let's make `name` our own name. To do this, we need to pass a unique **argument** when we actually call the function.
```python
def hello(name):
    print("Hello " + name)
hello("Emily")
```
Output:
`Hello Emily`

The `name` within the parenthesis when we define a function is called a **parameter**. When we pass data into the parenthesis while **calling** a function, it's called an **argument**.

For example, the function defined below utilizes a conditional statement to check if the input for the `name` variable contains a vowel, then uses a `for` loop to iterate over the letters in the `word` string.
```python
def has_vowel(word):
    # Check whether name has a vowel
    if set('aeiou').intersection(word.lower()):
        print(word, 'contains a vowel.')
    else:
        print(word, 'does not contain a vowel.')

has_vowel("supercalifragilisticexpialidocious")
has_vowel("why")
has_vowel("hey")
```
Output:
```
supercalifragilisticexpialidocious contains a vowel
why does not contain a vowel
hey contains a vowel
```
With parameters, we are able to use the same function with several different inputs.

### Keyword Arguments

In addition to calling parameters in order, you can use keyword arguments in a function call, in which the caller identifies the arguments by the parameter name.

When you use keyword arguments, you can use parameters out of order because the Python interpreter will use the keywords provided to match the values to the parameters.

Let's create a function that will show us profile information for a user. We'll pass parameters to it in the form of username (intended as a string), and followers (intended as an integer).
```python
def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))
```
Within the function definition statement, username and followers are contained in the parentheses of the profile_info() function. The block of the function prints out information about the user as strings, making use of the two parameters.

Now, we can call the function and assign parameters to it:
```python
def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))

# Call function with parameters assigned as above
profile_info("sammyshark", 945)

# Call function with keyword arguments
profile_info(username="AlexAnglerfish", followers=342)
```
Output:
```
Username: sammyshark
Followers: 945
Username: AlexAnglerfish
Followers: 342
The output shows us the usernames and numbers of followers for both users.
```
This also permits us to modify the order of the parameters, as in this example of the same program with a different call:
```python
def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))

# Change order of parameters
profile_info(followers=820, username="cameron-catfish")
```
Output:
```
Username: cameron-catfish
Followers: 820
```

## Default Argument Values

We can also provide default values for one or both of the parameters. Let's create a default value for the followers parameter with a value of `1`:
```python
def profile_info(username, followers=1):
    print("Username: " + username)
    print("Followers: " + str(followers))
```
Now, we can run the function with only the username function assigned, and the number of followers will automatically default to 1. We can also still change the number of followers if we would like.
```python
def profile_info(username, followers=1):
    print("Username: " + username)
    print("Followers: " + str(followers))

profile_info(username="JOctopus")
profile_info(username="sammyshark", followers=945)
```
Output:
```
Username: JOctopus
Followers: 1
Username: sammyshark
Followers: 945
```
Providing default parameters with values can let us skip defining values for each argument that already has a default.

## `return`

So far, we have printed everything to the console as a string. When creating functions, it is very common to want to do something with the result of a function. The `return` statement causes your function to exit and hand back a value to its caller. The point of functions in general is to take in inputs and return a value to its caller.

For example, here's a function utilizing both `print()` and `return`:

The following function, `square`, squares the parameter `x` and returns the variable `y`. We print out the value of `result`, which is created by calling the `square()` function with `3` passed as an argument.
```python
def square(x):
    y = x ** 2
    return y

result = square(3)
print(result)
```
Output: `9`

The output from square could be used by another line of code, like the following:
```python
def square(x):
    y = x ** 2
    return y

result = square(3) * 2
print(result)
```
Output: `18`

In the above code, we were able to use the value that `square(3)` returned and multiply it by two.
