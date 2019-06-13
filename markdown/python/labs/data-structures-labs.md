---
title: "data-structures-labs"
type: "lab"
---

# Data Structure Labs

Create a function called `shake_ball` that has no parameters. Inside the function, ask the user to ask a question about their future. Have your program **return** a **random** response of either: `Yes definitely`, `As I see it, yes`, `Ask again later`, `Cannot predict now`, `Don't count on it`, `Very doubtful`, and 4 other responses.

Call (invoke) the function like shown below:
```python
print(shake_ball())
```
Example output:
```
Ask a question: Will I be a millionaire?
Don't count on it
```

## Tuples Exercise

**Gymnast Scores**

Create a function called `gymnast_scores` that does not have any parameters or return anything. A gymnast can earn a score between 1 and 5 from each judge; nothing lower, nothing higher. All scores are integer values; there are no decimal scores from a single judge. Store the possible scores a gymnast can earn from one judge in a tuple.

1. **Print** out the sentence, "The lowest possible score is _ _ _, and the highest possible score is _ _ _." Use the values from your tuple. (Do not hard code the values)
    
2. **Print** out "A judge can give a gymnast _ points.". Filling in the blank with a random value from the tuple. (Do not hard code the value)

Call (invoke) the function like shown below:
```
gymnast_scores()
```
Example output:
```
The lowest possible score is 1, and the highest possible score is 5.
A judge can give a gymnast 3 points.
```

## Sets Exercises

**Remove Duplicates**

Create a function called `remove_duplicates` that takes in an iterable as a parameter and returns a set without any duplicates.

Call (invoke) the function like the example shown below:
```python
print(remove_duplicates('MISSISSIPPI'))
```
Example output:
```
{'M', 'P', 'S', 'I'}
```
**Finding Vowels**

Create a function called `finding_vowels` that takes in a string and returns `True` if there are **any** vowels in the word and `False` if there are not any vowels.

Call (invoke) the function like the example shown below:
```python
print(finding_vowels('mississippi'))
```
Example output:
```
True
```

## Dictionaries Exercises

**Polling friends**

Create a function called `polling_friends` that does not take in any parameters. In the function, create a dictionary called `fav_animals` where each key is a person's name, and each value is that person's response to the question "What is your favorite animal?". You are going ask your two friends "Miranda" and "Gordo". (Use user input to get their favorite animal). Store two responses in your dictionary. Return the dictionary once you are done!

Call (invoke) the function like shown below:
```python
print(polling_friends())
```
Example Output:
```
Gordo, what is your favorite animal? llama
>>>Miranda, what is your favorite animal? sloth
{'Gordo': 'llama', 'Miranda': 'sloth'}
```
**Birthday Month**

Create a function called `birthday_month` that takes in two parameters, `current` (representing the current month) and `birthday` (representing the user's birthday month) and returns the difference of the two months.

- Create a dictionary where each key is a month, and each value is the corresponding number for each month.
    
    - `months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}`
        
- Find the numerical value of `current` using the dictionary and store this is a variable called `curr_month_num`
    
- Find the numerical value of `birthday` using the dictionary and store this is a variable called `birth_month_num`
    
- Return the difference of the two months.
    

Call (invoke) the function like the example shown below:
```python
print(birthday_month('June', 'December'))
```
Example Output: `6`

* **Birthday Month Bonus:** calculate how many months in the **future** their birthday month is without loops or conditionals.
    - Examples:
        - If the current month is May and their birth month is August, you should return 3.
        - If the current month is May and their birth month is February, you should return 9.
        - If the current month is May and their birth month is May, you should return 0. (We are not concerned about days, just months)