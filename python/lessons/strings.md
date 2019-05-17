---
title: "strings"
type: "lesson"
---

# Strings

Down to basics: You can create a **string literal** by wrapping characters within single `'`, double `"`, or triple `"""` quotes. We'll be creating some string literals before trying to manipulate them.

Open up your Python Console. One way to get there is to Click on `Tools` \> `Python Console`.

In your Python Console, declare these variables with your first and last name and copy/paste the message to view the output:

Single quote example:
```python
group_name = 'Monty Python'
```
When using single-quotes for strings, be aware that they don't work in every situation. If I'm setting the sentence `'Monty Python's sketches are funny'` to a variable, we'll run into an error because of the apostrophe in `Python's`. In this case, we can use double-quote marks, but do you an alternative way to `print` this statement using single quotes?

Double quote example:
```python
statement = "Monty Python's sketches are funny"
```
Triple quote example:
```python
message = """This is a string that will span across multiple lines.
Using newline characters and no spaces for the next lines.
The end of lines within this string also count as a newline when printed"""
```
## Concatenation

Concatenation is the action of linking things together in a series.

We can re-write our "Hello world" program by **concatenating** strings and variables!
Let's set our variables in our program like so:
```python
english_greeting = "Hello"
say_hi_to = "world"
exclamation = "!"
```
Now call the print function at the bottom like so:
```python
english_greeting = "Hello"
say_hi_to = "world"
exclamation = "!"
print(english_greeting + say_hi_to + exclamation)
```
Notice that when we put variables within print functions they do not have `"` quotation marks around them. They're treated differently than **strings** within the print function.

You hopefully have a printed out statement that looks something like this: `Helloworld!`

How can we use the print statement to make it more human-readable?

Change the `+` signs to the following syntax:
```python
print(english_greeting, say_hi_to, exclamation)
```
But now we have `Hello world !` and we'd like the `!` to be directly after the word `world` without the space.

We can change about our `print()` statement to achieve this with:
```python
print(english_greeting, say_hi_to + exclamation)
```
Output: `Hello world!`

You can concatenate with the `+=` operator. This will concatenate the sequence with the right operand and assigns the results to that sequence.
```python
name = "Helga"
last_name = "Susan"
name += last_name
print(name)
```
Output: `HelgaSusan`

## Multiplying

We've already gone over how to use multiplication in Python, but did you know that Python can be used to multiply things other than numbers? In fact, you can use Python to multiply strings, which is actually pretty cool when you think about it. You can take a string and double, triple, even quadruple it with only a little bit of Python.

To multiply a string, this is the most straightforward way to go about doing it:
```python
print("hello" * 4)
```
Output: `hellohellohellohello`
```python
print("alright" * 3)
```
Output: `alrightalrightalright`

## Indexing

The index is a value we attach to a specific character in a string depending on its order.

If we had the following string: `greeting = "Hello World!"`, the index break down can be represented with the following:

| `H` | `e` | `l` | `l` | `o` |  | `W` | `o` | `r` | `l` | `d` | `!` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

The **index** of a character is the location of the character in the string, including spaces and punctuation. Indexes start counting with `0`.

For example, type and run the following:
```python
favorite_things = """Some of my favorite things are bird watching, jogging,
listening to podcasts, and coding in Python."""
```
Each of the individual characters has its own predetermined index as a result of the order it is in. Index `0`, also written as `[0]` is **always** the first character in a string. In this case, index `[0]` is the capital letter `S`

In a program, if we wanted to **only**`print()` the letter "S" we'd write it this way:
```python
print(favorite_things[0])
```
Output: `S`

First, call upon the variable we stored the string value in, and then specify the index of the character we're looking to print.

Type the above `print()` function into your Python Console and press `return`

## Slicing

We can use the index of a string to actually slice parts of that string out. The output of our `print()` statement can be manipulated depending on the indexes we specify.

To grab the first 10 characters of a string, use the following syntax:

string_name[start_index:stop_index]
This will start at the index that is specified before the colon and go up to (but not including) the stop_index.

Using our `favorite_things` variable, let's grab the first 10 characters from our string. Type this into our Python Console:
```python
print(favorite_things[5:10])
```
Output: `of my `

This slice shows the characters at indexes: `5, 6, 7, 8, 9`.

If we start at the beginning of a string (0 index), we do not have to place a value in front of the colon. This syntax would look like:
```
string_name[:stop_index]
```
Using this syntax with our `favorite_things` variable:
```python
print(favorite_things[:10])
```
To go to the end of the string, you could also just not place a value after the colon, like the following:
```python
string_name[start_index:]
```
Using this syntax with our `favorite_things` variable:
```python
print(favorite_things[31:])
```
Output: `bird watching, jogging, listening to podcasts, and coding in Python.`

Skipping characters is also possible by adding a `step` to the slice. This is done with the following syntax:
```
string_name[start_index:stop_index:step]
```
Using this syntax with our `favorite_things` variable, to only output every 2nd character of the whole string:
```python
print(favorite_things[::2])
```
Output: `Sm fm aoietig r idwthn,jgig itnn opdat,adcdn nPto.`

## The `in` Keyword

A helpful way of being able to check whether a string contains a specific item is the `in` keyword. This keyword returns a **boolean**.
```python
my_name = "Emily"
print("E" in my_name)
```
Output: `True`


## String Methods

### Finding the Length

If we take the image above and apply the built-in python function `len()` it will give us the length of the string.

Type the following into PyCharm:
```python
greeting = "HELLO WORLD!"
print(len(greeting))
```
Changing the Case

The functions `upper()` and `lower()` will return a string with all of the letters contained in the original string converted to either uppercase or lowercase.

Since strings are **immutable** data types, the returned string will be a **new** string and will have to be assigned to a new variable. Immutable means that once you have created the string, you cannot change any characters in the string to another value.

We can take the variable `greeting` that we set in the previous section, and make "HELLO WORLD" all lowercase:
```python
greeting = "HELLO WORLD"
print(greeting.lower())
```
In order to make the string `greeting` uppercase again, we can do as follows:
```python
print(greeting.upper())
```
A use case for manipulating strings in this way is if your users are entering their usernames in both upper and lowercase, we can still determine whether their name is in our database by checking it against an all uppercase version.

### `join()` method

This method will concatenate two strings in a way that passes one string through another. Here's an example:
```python
greeting = "HELLO WORLD"
```
We can add spaces to emphasize our greeting:
```python
new_greeting = " ".join(greeting)
print(new_greeting)
```
Output: `H E L L O W O R L D`

We can illustrate this another way but inserting dots between each character:
```python
greeting = "HELLO WORLD"
new_greeting = ".".join(greeting)
print(new_greeting)
```
Output: `H.E.L.L.O. .W.O.R.L.D`

This method is useful to combine a list of separate strings into a new single string. We're telling join to insert a comma to join the separate strings into one single string.
```python
greetings = ["hello", "hola", "salve"]
string_greeting = ",".join(greetings)
print(string_greeting)
```
Output: `"hello,hola,salve"`

If we put a space (`" ".join(greetings)`) instead of a comma (`",".join(greetings)`), the output would be a single string with spaces separating each word (`hello hola salve`).

### `split()` Method

Split will do the opposite of what we just did with the join method. We'll start with a string of things separated with spaces and **split** it into a list of strings.
```python
greetings = "hello hola salve"
string_greeting = greetings.split()
print(string_greeting)
```
Output: `['hello', 'hola', 'salve']`

We can also remove a specific character from a string by using the split method, which also splits the string at the location of the designated character, like so:
```python
print(greetings.split("l"))
```
Output: `['he', '', 'o ho', 'a sa', 've']`

### `replace` Method

The `replace()` method can take an original string and return an updated string with some specific replacement.

Since Latin is a dead language, we want to replace `"salve"` with the Italian greeting `"ciao"`:
```python
greetings = "hello, hola, salve"
new_greeting = greetings.replace("salve", "ciao")
print(new_greeting)
```
Output: `"hello, hola, ciao"`

### Reversing Strings

You may want to reverse a string to check to see if a word is a palindrome - spelled the same way backward and forward.

One way of doing so would be to use **slicing**. We went over slicing previously, and if you recall the way to get the **last** character in a string, is to call upon `string\$&-1]` since -1 represents the last character in the index of the string.

The syntax to tell Python to not only print out the last character, but also the rest of the characters in the string **backwards** is to use double colon: `::` before the `-1` as follows:
```python
greeting = "Hello"[::-1]
print(greeting)
```
A way to reverse a string without using lists is `join()` and `reversed()` together.
```python
string = "HELLO"
reversed_string = ''.join(reversed(string))
print(reversed_string)
```
In this case we're taking a string, setting it to variable `string` and `join()` is merging all of the characters resulting from the reversed iteration into a **new** string.

It can also be written like so:
```python
reversed_string = ''.join(reversed("HELLO"))
print(reversed_string)
```
Regardless of whether or not you set the original string to a variable, since a new string is formed from the `join()` method, it has to be set to a variable in order to save the reversed string to memory in order to be printed out.

## Applying your knowledge

Describe the sketch comedy group

* Create a variable with their name (Monty Python)
* Create a short description in the form of a string assigned to a variable (Monty Python was a British comedy group)
* Create a variable assigned to a number that represents the year they were formed (1969)

Introduce the group in a sentence
* Assign a variable whose value will be a concatenation of the above variables into a sentence that makes sense.
* Using the above variables, write the sentence in two different ways that we have learned to concatenate strings, numbers and variables in a print() statement to avoid a TypeError (Hint: Use + and ,)

Strings follow-along

1. Create a string called `phrase` that is set to the value of `Don't count your chickens before they hatch`
    
2. Create a second string called `slogan` that is set to the value of `For Everything Else, There's MasterCard`
    
3. Create a third string called `combined` that is equal to `phrase`, a period(`.`), and `slogan` concatenated. Print out the new value of `combined`
    
4. Print out phrase three times in a row. Do this with the multiplying strings method.
    
5. Print out the 7th character in `slogan`
    
6. Print out the last character in `combined`
    
7. Print out every other letter in `phrase`
    
8. Print out the 17th - 24th indexes (inclusive) of `phrase`
    
9. Print out every other letter in `combined`
    
10. Print out if it is `True` or `False` that the letter `m` is in `slogan`. (Do not hard code. Use the `in` operator)
    
11. Print out the value of `combined`, but in all caps
    
12. Print out `combined` split up by spaces
    
13. Print out `slogan` backwards
    