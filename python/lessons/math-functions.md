---
title: "math-functions"
type: "lesson"
---

# Math Functions

Python has a `math` library that comes with several functions that allow for additional mathematical operations. To use these functions, you must `import math` at the top of every file.

<table>

<tr><td> <code>abs()</code> </td> <td>Gets the absolute value of a float or int</td> <td>
<code>
print(90 - 120) 
print(abs(90 - 120))
</code>

Output:

`-30`

`30`


</td> </tr>
<tr><td> <code>pow()</code> </td> <td>Raises a number to a certain power</td> <td>

<code>
print(pow(2,3))
</code>
Output:

`8`

</td> </tr>
<tr><td> <code>round()</code></td> <td>Rounds a number to a certain decimal point </td> <td>

<code>
print(round(17.34989436516001,4))
</code>
Output:

`17.3499`

</td> </tr>
</table>

## Random Values

Using the **random** module, we can generate psuedo-random numbers. To use the **random** module, you must place the following at the top of your file:

`import random`

<table>
<tr><td width="15%">Function</td><td width="35%">Description</td><td>Example</td></tr>
<tr><td> <code>random</code></td><td width="50%">Generates a random number floating point number between 0 and 1 </td><td>

<code>
print(random.random())
</code>
Possible Output:
`0.173499`

</td></tr>
<tr><td> <code>randint</code></td><td>Generates a random whole number between two numbers (inclusive)
</td><td>

Choosing a random whole number between 1 and 100

<code>
print(random.randint(1, 100))
</code>
Possible Output:
`95`
</td></tr>
<tr><td> <code>uniform</code></td><td>Generates a random floating point number between two numbers (inclusive)</td><td>

Choosing a random floating point number between 10 and 50

<code>
print(random.uniform(10, 50))
</code>
Possible Output:
`24.313911327373457`

</td></tr>
<tr><td><code> choice </code></td><td> Generates a random value from an iterable</td><td>
Choosing a random value from a list of numbers 

`90, 12, 34`

<code>
print(random.choice([90, 12, 34]))
</code>
Possible Output:
`12`

</td> </tr>
</table>