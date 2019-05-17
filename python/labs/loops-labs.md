---
title: "loops-labs"
type: "lab"
---

# Loop Lab

## Create String

```python
letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']
```

Create a function that is called `create_string` that does not have any parameters. Using a `for` loop, convert the above list `letters` into a single string and return the string. Do not just print the letters out side by side

Place the following at the bottom of your `main`:
```python
print(create_string())
```
Example output:
```
Orange Method
```
## Filling Tickets

Define a function `fill_ticket()` that will ask a user five times to insert a number. (Use a loop to do this). After every time they answer, their newest answer is placed at the end of a list. This list is then returned.

Place the following at the bottom of your `main`:
```python
guesses = fill_ticket()
print(guesses)
```
Example Output:
```
Enter a number: 5
Enter a number: 1
Enter a number: 3
Enter a number: 4
Enter a number: 1
[5, 1, 3, 4, 1]
```
## Finding Matches

The winning combination of this lottery is chosen by picking five numbers. Define a function `matches(ticket, winners)` that takes two lists and returns an integer that says how many numbers the two lists are in the **exact same position**.

Copy and paste the code below at the bottom of your main function to test out your `matches(ticket, winners)` functions.
```python
guesses = fill_ticket()

winners = [1, 2, 3, 4, 5]
print(matches(guesses, winners))
```
Output:
```
Enter a number: 5
Enter a number: 1
Enter a number: 3
Enter a number: 4
Enter a number: 1
2
```
## Caesar Cipher

In cryptography, a Caesar cipher is a very simple encryption technique in which each letter in plain text is replaced by a letter of some fixed number of positions further down the alphabet. For example, with a shift of 3, `A` would store it in variable `D`, `B` would become `E`, and so on. The method is named after Julius Caesar, who used it to communicate with his generals. He used a shift of 13.

`cipher_key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}`

Create a function called `caesar_cipher` that takes in a string and then returns the string changed with a shift of 13 letters. Note: your dictionary only works with lower case letters

Place the following at the bottom of your `main`:

print(caesar_cipher("pnrfne pvcure? v zhpu cersre pnrfne fnynq!"))
To figure out the answer, you must complete the exercise!

# While Loops

## Dice Histogram - While Loops Style

Alter the previous histogram code to create a histogram with the results of rolls of a 6-sided dice. Stop "rolling the dice" once your random number is 4.

## Guessing Game

Create a program that will ask the user to guess a **random** number between 1 - 20. Keep asking the user until they guess it correctly.

## Credit Limit

Create a program that has the user first set a value for their bank account balance. Then ask the user to enter a new amount that they just spent and subtract this value from the total. Once they reach a zero balance, print out `"All out of money!"`. If they reach a negative balance, raise a `RuntimeError`.

Example Output:
```
Enter Account Balance: 100
>>> Enter Amount Spent: 55
Amount Left: 45
>>> Enter Amount Spent: 20
Amount Left: 25
>>> Enter Amount Spent: 30
Amount Left: -5
All out of money!
```

## Pig Latin

Create a function called `pig_latin` that receives a String called `pig` and return `pig` in pig latin.

Here's how to translate the English word into the Pig Latin word:

- If there are no vowels in englishWord, then pigLatinWord is just `englishWord + "ay"`. (There are ten vowels: `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and their uppercase counterparts. `y` is not considered to be a vowel for the purposes of this assignment, i.e. `my` becomes `myay`, `why` becomes `whyay`, etc.)
    
- Else, if englishWord begins with a vowel, then pigLatinWord is just `englishWord + "yay"`
    
- Otherwise (if englishWord has a vowel in it and yet doesn't start with a vowel), then pigLatinWord is `end + start + "ay"`, where `end` and `start` are defined as follows:
    
    
    - Let `start` be all of englishWord up to (but not including) its first vowel.
        
    - Let `end` be all of englishWord from its first vowel on.
        
    