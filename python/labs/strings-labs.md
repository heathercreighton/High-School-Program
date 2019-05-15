---
title: "strings-labs"
type: "lab"
---
It is very common to check if a character is a letter or not. In Python, have a user enter a character and check to see if it is a letter or not (Either upper or lowercase).

Example Output 1:
```
>>> Enter a character: i
True
```
Example Output 2:
```
>>> Enter a character: @
False
```

## Short Hand

Create a function called `short _hand` that takes in a String called `short` and return `short` in short hand. The simplified shorthand form of a String is defined as follows:

- replace these four words: "and" with "&", "too" with "2", "you" with "U", and "for" with "4".
    
- remove all vowels ('a', 'e', 'i', 'o', 'u', whether lowercase or uppercase). **Be careful on removing `U`!**
    

Place the following at the bottom of your `main`:
```python
print(short_hand("Thank you for that! You are too sweet and kind!"))
```
Example output:
```
Thnk U 4 tht! U r 2 swt & knd!
```
## Credentials Generator

We want to create a random credential generator using a combination of string skills, random numbers and concatenation. All input to the algorithm must be at least three characters long. Your program should first ask the user for:

- their first name
    
- last name
    
- city they were born
    
- university they graduated from
    
- a name of a relative
    
- a name of a friend
    

Using all of the information the user has typed in, start the creation of their credentials.

**Their employee id is generated with the following concatenated:**

1. the first three letters of your first name
    
2. the last two letters of your last name
    

**Their user name is generated with the following concatenated:**

1. the first two letters of the city you were born in
    
2. the last three letters of the university they graduated from
    

**Their password will be more randomly generated with the following concatenated:**

1. starting at a random location to the end of your relative's name.
    
2. starting at the beginning of your friend's name to a random location of the string.
    

Example Output:
```
Enter First Name: Sally
>>> Enter Last Name: Rodgers
>>> Enter Birth City: Austin
>>> Enter Alma Mater University: Texas A&M University
>>> Enter a Relative's Name: Joe
>>> Enter a Friend's Name: Elissa

Employee ID: Salrs
User Name: Auity
Password: Oeeli
```
**BONUS:** In the output, capitalize **only** the first letter, formatted like a proper name: "Emiton"

## Remove Case and Punctuation

Create a program that has the user enter a string of any length. Change the case of every letter to lower case and remove all of the occurrences of symbols and spaces.

Example Output:
```
>>> Enter a phrase: Madam, I'm Adam
madamimadam
```
## Palindrome

A palindrome is a word that can read the same forwards and backwards. Continue the program "Remove Case and Punctuation", with the newly altered string print `True` if the string is a palindrome and `False` if it is not. The idea of a palindrome can be extended to phrases or sentences if we ignore details like punctuation and case.

Example Outputs:
```
>>> Enter phrase: Madam, I'm Adam
Palindrome? True

>>> Enter phrase: Computer
Palindrome? False
```