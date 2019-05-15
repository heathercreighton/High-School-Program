---
title: "math-variables-labs"
type: "lab"
---
**Can a swallow carry a coconut?**

This Monty Python-inspired math problem

Assuming a swallow weighs 60 grams, and one swallow is capable of carrying 1/3 of its own weight…​ Can a swallow carry a coconut, average weight being 1450 grams?

---

1. Write the equation to determine how many grams total a single swallow is capable of carrying, include the answer.

2. Write the equation to determine how many swallows it will take to carry a coconut weighing 1450 grams.

3. Write the above equation in a single line, instead of two separate steps, and include the answer.

---

**What other fruit can a swallow carry?**

Swallows per coconut: `1450 / (60 / 3) = 72.5`

Swallows per apple: `128 / (60 / 3) = 6.4`

Swallows per cherry: `8 / (60 / 3) = 0.4`

After all of our intensive calculations, we've finally found that a single swallow has the ability to carry a cherry!

If we look at our equations, we can see a lot of **repetition**. One thing programmers hate is repeating their code over and over so they use a handy-dandy thing called a **variable** to make equations (and code) easier to read and write. Which part of the three above equations is being repeated?

## Macaw Exercise

**Can a macaw carry a coconut?**

Using IDLE, declare a variable for each value and find out the macaw's carrying limit:

1. The percentage of the weight they can carry (Given value: 1/3)
2. The coconuts weight (Given value: 1450)
3. The macaw's weight (Given value: 900)
4. Variable for number of macaws required
5. Print the number of macaws required to carry a coconut
Click to Reveal Answer

* * *

Ultimately, we need 4.8 macaws to carry a coconut. This gives us a more difficult issue, since we can't summon 0.8 of a bird, so we'd like to be able to round that number up for a more reasonable answer we can actually work with.

## Using PyCharm to write our first program

Python has many modules at our disposal which can a make more difficult math problems seem like a breeze. In order to use **any** module in Python, we `import` it like so:
```
import math
```
Open the project `python-foundations`, then right-click it again and go to New → Python File and enter `math_variables` as the file name. PyCharm will automatically add the `.py` for this file.

Type `import math` on the first line of the file. We can look at the math module documentation to on check which function we want to use for our specific problem: [Python Math Library Documentation](https://docs.python.org/3.0/library/math.html)

You don't have to scroll down very far on the page to see that the math library offers a `math.ceil()` function which will return the smallest number greater than or equal to the value you put inside the parenthesis.

Let's try it! In your PyCharm, type out and run the following:
```python
import math
num_macaws = 4.8
math.ceil(num_macaws)
```
We see that the program runs, but it's not giving us any output. In order to actually **see** our result, we have to use a function we haven't introduced yet: the `print()` function. Re-run the program but put `math.ceil(num_macaws)` inside a `print()` function, and view the output.

Our entire `macaw` program looks like this:
```python
import math
carrying_weight_percentage = 1/3
coconut_weight = 1450
macaw_weight = 900
macaw_limit = macaw_weight * carrying_weight_percentage
number_macaws = coconut_weight/macaw_limit
print(math.ceil(number_macaws))
```
