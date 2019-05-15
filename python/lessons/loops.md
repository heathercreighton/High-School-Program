---
title: "loops"
type: "lesson"
---
numbers = [10, 5, 2, 7]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
```
That is a lot of lines! We should not ever have to repeat the same action over and over again. This is where loops come in to play.

## For loops

For loops are used to repeat the same action a known number of times. A for loop can help with printing out all the values of any **iterable**.
An iterable is an item that is capable of returning its members one at a time, such as a list, tuple, or string. Indentation is very important!
Indentation tells the Python interpreter what belongs together. In the loops case, it tells the Python Interpreter which line(s) to repeat.

### Set Up

In Python, for loops are constructed like so:
```
for [iterating variable] in [iterable]:
  [do something]
```
**iterating variable** : the temporary name of the current element. This can be called any valid variable. It's best practice not to name this the same name as another existing variable.

**iterable** : the iterable that you are looping through it's elements

**do something** : any action that you are wanting to repeat

Example 1: For loop going through a list, printing each item on the same line
```python
for i in [10, 5, 2, 7]:
  print(i, end = " ")
```
Output: `10 5 2 7`

`i` represents the iterating variable and holds the value of the element that is currently being used. It will be assigned to each element in turn for each **iteration** through the loop.
An iteration is what number time you have repeated the action in the loop.

Reminder: `end = " "` prints all of the numbers on the **same line** with a space in between.

Example 2: For loop printing the numbers 1, 2, 3, 4 each on the same line
```python
for x in [1, 2, 3, 4]:
  print(x, end = " ")
```
Output: `1 2 3 4`

Example 3: For loop going through a list called numbers, printing each item on the same line
```python
numbers = [20, 30, 40, 50]
for k in numbers:
  print(k, end = " ")
```
Output: `20 30 40 50`

Example 4: For loop going through a string called name, printing each character on the same line
```python
name = "Betty"
for w in name:
  print(w, end = " ")
```
Output: `B e t t y`

Example 2 leads to a need for a new function because counting from one number to the next is a very common need in development. What if you wanted to print out the numbers 1 through 100?
If we did it the way shown above, you would have to physically type 100 numbers and commas! This is where range can help us out.

### Range

Range is a handy function that creates lists in the following format:
```
range([start,] stop [,step])
```
The above square brackets, in this case, are used to mean "This is optional". When both step and stop are not specified, the list will start at 0, step by 1's, and go up to but not including stop.
When start and stop are specified, the list starts at start, goes up by 1's, and up to but not including stop.
When all three values are specified, the list will start at start, go up by step, and go up to but not including stop. Below are some examples showing different uses for range.

Example 1: Using just stop
```python
range(4)
```
The list generated above would be `[0, 1, 2, 3]`

Example 2: Using just start and stop
```python
range(1, 4)
```
The list generated above would be `[1, 2, 3]`

Example 3: Using start, stop, and step
```python
range(1, 10, 2)
```
The list generated above would be `[1, 3, 5, 7, 9]`

**For Loops with Range**

If we combine the two concepts of for loops and range together, we can do things way more efficiently!

Example 1: For loops using Range
```python
for i in range(2, 10, 3):
  print(i, end = " ")
```
Output: `2 5 8`

Example 2: For loops using Range as a counter
```python
# Say you wanted to repeat the word "OM" 5 times
for i in range(5):
  print("OM", end = " ")
```
Output: `OM OM OM OM OM`

### For Loops using Operations

There is often a need for the same operation to be done on or with every item in a list or tuple. For loops allow you to this:

Example 1: Squaring every element in a list
```python
prices = [12, 7, 9, 10]
for i in prices:
  print(i ** 2, end = " ")
```
Output: `144 49 81 100`

Example 2: Finding the total of a list
```python
prices = [12, 7, 9, 10]
total = 0
for i in prices:
  total += i
print(total)
```
Output: `38`

Example 2 is a little different than what we have seen before. Every iteration, we added on the current element in the list to it.

- The first iteration added the first item (12) in the list to total, change total's value to 12.
    
- The second iteration added the second item (7) in the list to total, change total's value to 19.
    
- The third iteration added the third item (9) in the list to total, change total's value to 28.
    
- The fourth and final iteration added the fourth item (10) in the list to total, change total's value to 38.
    

### `enumerate`

So far, we have just wanted to either loop through a list OR use range to count. `enumerate` adds a counter to an iterable and returns it.

**enumerate Set Up**
```
enumerate(iterable, start=0)
```

* **iterable:** a sequence, an iterator, or objects that supports iteration  
* **start:** (optional) starts counting from this number. If start is not provided, the count will start at 0.
    

**enumerate Examples**
```python
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

for count, item in enumerate(grocery, 100):
  print(count, item)
```
Output:
```
(0, 'bread')
(1, 'milk')
(2, 'butter')

0 bread
1 milk
2 butter

100 bread
101 milk
102 butter
```
### Applying your knowledge

1. Create a `for` loop that prints off the numbers `89`, `41`, `73`, and `90` \- each on their own line
    
2. Create a `for` loop that prints off the numbers 5 up-to but not including 15
    
3. Create a `for` loop that prints off the numbers 100 to 200 by 10's
    
4. Create a `for` loop that prints off the numbers from 80 to 32 by 8's
    
5. Create a `for` loop that prints off the word `Alright` three times.
    
6. Create a `for` loop that creates the following image:
    

Using `range`, create a `for` loop that prints off the numbers 1, 4, 9, 16.

**8.** Create a `for` loop that goes through a list and counts the number of even and odd numbers. Use the following list as an example to work with: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]`

Output:
```
Even numbers: 4
Odd numbers: 5
```
Change the following starter code to choose a random number between 1 and 6 one hundred times and display it on the histogram:
```python
import matplotlib.pyplot as plt
import random

a = []  # create an empty list

for roll in range(5):
    x = random.choice([1, 3, 10])  # choose a random choice of either 1, 3 or 10 to a (the list)
    a += [x]

plt.hist(a, range=(1, 10), align='right')  # options for aligning are 'mid', 'left', and 'right'
plt.show()
```

## While Loops

While Loops are used when the same task needs to happen until a condition is met. The code that is in a `while` block will execute as long as the `while` statement evaluates to True.
For example, when a user is typing in their password the login screen will remain up until the user types in the correct password. Who knows how many times they might type it in wrong!
As opposed to for loops that execute a certain number of times, while loops are conditionally base, so you don't need to know how many times to repeat the code going in.

### Set Up

In Python, while loops are constructed like so:
```
while [a condition is True]:
  [do something]
```
**a condition is True** : a boolean statement that determines if you go into the loop or not.

**do something** : any action that you are wanting to repeat

Example 1: While loop that repeats until the temperature of tea is at 112
```
temperature = 115
while (temperature > 112):
  print(temperature, end = "-")
  temperature -= 1
print('The tea is cool enough')
```
Output: `115-114-113-The tea is cool enough`

Example 2: While Loop that repeats the phrase "Waiting" until a user presses the x key
```python
x_input = input("Enter the x key: ")
while (x_input != "x"):
  print("Waiting")
  x_input = input("Enter the x key: ")
print("Thank you for typing x!")
```
The output of Example 2 varies depending on that the user types in. Two example outputs are show below:

Example 2 Output 1: User types in two incorrect inputs before typing in x.
```
Enter the x key: hi
Waiting
Enter the x key: y
Waiting
Enter the x key: x
Thank you for typing x!
```
Example 2 Output 2: User types in x the first loop.
```
Enter the x key: x
Thank you for typing x!
```

### Common Mistakes

Be VERY careful about infinite loops! This occurs when your condition would never return False. Two examples of this are shown below:
```python
while True:
  print("Ah!")

while 5 == 5:
  print("Forever looping!")
```
Both of these loops would go on forever!

### Applying your knowledge

1. Create a `while` loop that will count down from 10 to 1.
    
2. Asks the user to enter an integer that is greater than 0. The function will keep on asking the user for the number until it is valid.
    
3. Ask the user to enter two separate integers (The first number must be smaller than the second). Create a while loop that will count from the first number to the second.
    
4. Ask the user to respond by 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'. The function keeps on asking until the user enters the correct information.
    

### Error handling with a while loop exercise

Given this `while` loop, write a try/except statement. The input of the users guess can only be a whole number. Make sure the `except` throws an error (One exception total) for both floating point numbers and letters.
```python
count = 0
while count < 5:
    guess = int(input("Take a guess "))
    count = count + 1
```