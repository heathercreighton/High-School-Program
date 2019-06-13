---
title: "classes-labs"
type: "lab"
---

# Classes Labs

Create a new file called `string_manipulation.py`.

Inside your new file, create a class called `StringManipulation`. Inside this class create the following methods.

**Constructor**

Create a constructor that takes in a string called `altering_str`.

**String Reversal**

Create a function called `string_reversal` that takes in a String called `reverse` that has a default value of 'None'. If the value of `reverse` remains `None`, return `self.altering_str` reversed. If the value of `reverse` has changed, return the exact reversal of the characters in the new string.

**Removing Case**

Create a function called `removing_case` that takes in a String called `removed` that has a default value of 'None'. If the value of `removed` remains `None`, return `self.altering_str` without any punctuation, spaces and all letters are converted to lowercase. If the value of `removed` has changed, return `removed` without any punctuation, spaces and all letters are converted to lowercase.

**Is Vowel**

Create a function called `is_vowel` that takes in a String called `searching` that has a default value of 'None'. If the value of `searching` remains `None`, return if `self.altering_str` contains any vowels. If the value of `is_vowel` has changed, return if `is_vowel` contains any vowels.

**Palindrome**

Create a function called `is_palindrome` that takes in a String called `searching` that has a default value of 'None'. If the value of `searching` remains `None`, return if `self.altering_str` is a palindrome. If the value of `is_palindrome` has changed, return if `is_palindrome` is a palindrome.

**Short Hand**

Create a function called `short_hand` that takes in a String called `short` that has a default value of 'None'. If the value of `short` remains `None`, return if `self.altering_str` in shorthand. If the value of `short` has changed, return `short` in short hand. The simplified shorthand form of a String is defined as follows:

- replace these four words: "and" with "&", "to" with "2", "you" with "U", and "for" with "4".
    
- remove all vowels ('a', 'e', 'i', 'o', 'u', whether lowercase or uppercase). **Be careful on removing `U`!**
    

**Pig Latin**

Create a function called `pig_latin` that receives a String called `pig`, that has a default value of 'None'. If the value of `pig` remains `None`, return if `self.altering_str` in pig latin. If the value of `pig` has changed, return `pig` in pig latin.

Here's how to translate the English word into the Pig Latin word:

- If there are no vowels in englishWord, then pigLatinWord is just `englishWord + "ay"`. (There are ten vowels: `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and their uppercase counterparts. ‘y' is not considered to be a vowel for the purposes of this assignment, i.e. `my` becomes `myay`, `why` becomes `whyay`, etc.)
    
- Else, if englishWord begins with a vowel, then pigLatinWord is just `englishWord + "yay"`
    
- Otherwise (if englishWord begins has a vowel in it and yet doesn't start with a vowel), then pigLatinWord is `end + start + "ay"`, where `end` and `start` are defined as follows:
    
    
    - Let `start` be all of englishWord up to (but not including) its first vowel.
        
    - Let `end` be all of englishWord from its first vowel on.
