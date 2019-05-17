---
title: "data-structures"
type: "lesson"
---

# Data Structures

## Lists

A **list** is a data structure in Python that is a **mutable**, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets `[ ]`.

Lists are great to use when you want to work with many related values. They allow you to keep data together that belongs together, condense your code, and perform the same methods and operations on multiple values at once.

Example: Creating a list of strings called dogs
```python
dogs = ["Collie", "Labrador", "Sheltie", "Dalmatian"]
```
When you print out the list, the output looks exactly like the list we created:
```python
print(dogs)
```
Output: `["Collie", "Labrador", "Sheltie", "Dalmatian"]`

### Length

`len()`, just like in a string, allows you to find the number of elements that are in a list. Do the following to find the length of a list:
```python
dogs = ["Collie", "Labrador", "Sheltie", "Dalmatian"]
print(len(dogs))
```
Output: `4`

Keep in mind that `len`gth starts counting at 1

### Indexing

As an ordered sequence of elements, each item in a list can be called individually, through **indexing**. Lists are a compound data type made up of smaller parts, and are very flexible because they can have values added, removed, and changed. When you need to store a lot of values or iterate over values, and you want to be able to readily modify those values, you'll likely want to work with list data types.

Each item in a list corresponds to an index number, which is an integer value, starting with the index number 0. (Just like string's indexing)

For the list dogs, the index breakdown looks like this:

| Collie | Labrador | Sheltie | Dalmatian |
| :---: | :---: | :---: | :---: |
| 0 | 1 | 2 | 3 |

The first item, the string `Collie` starts at index 0, and the list ends at index 4 with the string `Dalmatian`.

Because each item in a Python list has a corresponding index number, we're able to access and manipulate lists in the same ways we can with other sequential data types.

We can call a specific item of the list by referring to its index number:
```python
print(dogs[1])
```
Output: `Labrador`

The index numbers for this list range from 0 - 3, as shown in the table above. So if we tried to access a value greater than this, we would get an Out Of Range error!
```python
print(dogs[10])
```
Output: `IndexError: list index out of range`

It is very common to need the last item in a list. If a boss needs to fire the person with the lowest number of sales, they could find this in a sorted list that is in descending order of sales. To easily find the last item in a list, we can access from the list with a negative index number, by counting backwards from the end of the list, starting at -1. This is especially useful if we have a long list and we want to pinpoint an item towards the end of a list.

For the same list `dogs`, the negative index breakdown looks like this:

| Collie | Labrador | Sheltie | Dalmatian |
| :---: | :---: | :---: | :---: |
| -4 | -3 | -2 | -1 |

So, if we would like to print out the item `Sheltie` by using its negative index number, we can do so like this:
```python
print(dogs[-2])
```
Output: `Sheltie`

We can concatenate string items in a list with other strings using the `+` operator.
```python
print("Charlie is a " + dogs[1])
```
Output: `Charlie is a Labrador`

### Slicing

We can also call out a few items from the list. Let's say we would like to just print the middle items of `dogs`, we can do so by creating a slice. With slices, we can call multiple values by creating a range of index numbers separated by a colon `[start_index: stop_index]`
```python
print(dogs[1: 3])
```
Output: `["Golden Retriever", "Sheltie"]`

When creating a slice, as in `[1: 3]`, the first index number is where the slice starts (inclusive), and the second index number is where the slice ends (exclusive), which is why in our example above the items at position 1 and 2 are the items that print out.

* * *

If we want to include either end of the list, we can get rid of the numbers in the `list[x: y]` syntax. For example, if we want to print the first 2 items in the list `dogs` \- which would be `Collie` and `Golden Retriever` \- we can do so by typing:
```python
print(dogs[: 2])
```
Output: `["Collie", "Golden Retriever"]`
This list printed off the list items with indexes starting with 0 and going up to (but not including) 2.

* * *

To include all the items at the end of a list, we would reverse the syntax:
```python
print(dogs[2: ])
```
Output: `["Sheltie", "Dalmatian"]`
This list printed off the list items with indexes starting with 2 and going to the end of the list.

One last thing that we can use with slicing is the **step**. Step is how many items to move forward after the first item is retrieved from the list. Before this point, we have not used the step parameter, meaning we are using the default step value of one.

* * *

This syntax for this construction is `list[x: y: z]`, with z referring to stride. Let's make a larger list, then slice it, and give the step a value of 2:
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1: 11: 2])
```
Output: `[1, 3, 5, 7, 9]`

The above example starts at index 1, goes up to (but not including) 11, going up by 2's (every other item).

* * *

We can omit the first two parameters and use step alone with the syntax `list[: : 2]`
```python
print(numbers[: : 3])
```
Output: `[0, 3, 6, 9]`

* * *

We can print the list backwards with a negative step
```python
print(numbers[: : -2])
```
Output: `[10, 8, 6, 4, 2, 0]`

### Modifying

We can use indexing to change items within the list, by settling an index number equal to a different value. This gives us greater control over lists as we are able to modify and update the items that they contain.

If we want to change the string value of the item at index 1 from `Labrador` to `Golden Retriever`, we can do so like:
```python
dogs[1] = "Golden Retriever"
```
Now if we print out `dogs`, we can see the updated values.
```python
print(dogs)
```
Output: `["Collie", "Golden Retriever", "Sheltie", "Dalmatian"]`

#### Adding

Operators can be used to make modifications to lists. The `+` operator can be used to concatenate two or more lists together:
```python
first_names = ["Noelle", "Tereza", "Raelin", "Linus"]
last_names = ["Blossom", "Chrissy", "Grover", "Devin"]
print(first_names + last_names)
```
Output: `["Noelle", "Tereza", "Raelin", "Linus", "Blossom", "Chrissy", "Grover", "Devin"]`

Because the `+` operator can concatenate, it can be used to add an item (or several) in list form to the end of another list.
```python
first_names = first_names + ["Sally"]
print(first_names)
```
Output: `["Noelle", "Tereza", "Raelin", "Linus", "Sally"]`

`+` and \* operators have a compound forms `+=` and `\*=`. So the above example can also be written as:
```python
first_names += ["Sally"]
print(first_names)
```
Output: `["Noelle", "Tereza", "Raelin", "Linus", "Sally"]`

* * *

If you do not place the brackets around the string you are adding, the following will happen:
```python
first_names += "Sally"
print(first_names)
```
Output: `['Noelle', 'Tereza', 'Raelin', 'Linus', 'S', 'a', 'l', 'l', 'y']`

This is because Python will take the string as a list of characters, therefore adding the characters one at a time.

#### Removing

Items can be removed from lists by using the `del` statement. This will delete the value at the index number you specify within a list.

From the `dogs` list, let's remove the item "Sheltie". This item is located at the index position of 2. To remove the item, we'll use the del statement then call the list variable and the index number of that item:
```python
dogs = ["Collie", "Golden Retriever", "Sheltie", "Dalmatian"]
del dogs[2]
print(dogs)
```
Output: `["Collie", "Golden Retriever", "Dalmatian"]`

We can also specify a range with the `del` statement. Say we wanted to remove not only the item "Sheltie", but also "Dalmatian" as well. We can call a range in `dogs` with the del statement to accomplish this:
```python
dogs = ["Collie", "Golden Retriever", "Sheltie", "Dalmatian"]
del dogs[2: ]
print(dogs)
```
Output: `["Collie", "Golden Retriever"]`

### List Methods

List has several **methods** that are very helpful. We are going to briefly cover some of the list methods that are available.

##### list.append()

The method `list.append(x)` will add an item `(x)` to the end of a list.
```python
fish = ["barracuda", "cod", "devil ray", "eel"]
```
This list is comprised of 4 string items, and their index numbers range from 'barracuda' at 0 to 'eel' at index 3.

Adding flounder to the List
```python
fish.append('flounder')
print(fish)
```
Output: `['barracuda', 'cod', 'devil ray', 'eel', 'flounder']`

Now, we have a list of 5 string items that ends with the item we passed to the `.append()` method.

It is also possible to add a list to the end of a list

Adding a list inside a List
```python
fish.append(['flounder', 'clown'])
print(fish)
```
Output: `['barracuda', 'cod', 'devil ray', 'eel', ['flounder', 'clown']]`

Now, we have a list of 5 string items that ends with the list we passed to the `.append()` method.

##### list.extend()

The method `list.extend(x)` acts similarly to `list.append(x)`. This method adds element(s) (notice it can be plural!) to a list by adding the element(s) of the item you pass to it. The resulting list is one containing all of the elements of both lists.
```python
fish = ["barracuda", "cod", "devil ray", "eel"]
```
This list is comprised of 4 string items, and their index numbers range from 'barracuda' at 0 to 'eel' at index 3.

Adding flounder to the List
```python
fish.extend('flounder')
print(fish)
```
Output: `['barracuda', 'cod', 'devil ray', 'eel', 'flounder']`

Now, we have a list of 5 string items that ends with the item we passed to the `.extend()` method.

It is also possible to add a list to the end of a list

Appending a list to the end a List
```python
fish.extend(['flounder', 'clown'])
print(fish)
```
Output: `['barracuda', 'cod', 'devil ray', 'eel', 'flounder', 'clown']`

This is where the difference of `append()` and `extend()` is seen.

##### list.insert()

The `list.insert(i,x)` method takes two arguments, with i being the index position you would like to add an item to, and x being the item itself.

Our aquarium acquired another new fish, an anchovy. You may have noticed that so far the list fish is in alphabetical order. Because of this, we don't want to just add the string 'anchovy' to the end of fish with the list.append() method. Instead, we'll use `list.insert()` to add 'anchovy' to the beginning of this list at index position 0:
```python
fish.insert(0, 'anchovy')
print(fish)
```
Output: `['anchovy', 'barracuda', 'cod', 'devil ray', 'eel', 'flounder']`

In this case, we added the string item to the front of the list. Each of the successive items will now be at a new index number as they have all moved down. Therefore, 'barracuda' will be at index 1, 'cod' will be at index 2, and 'flounder' — the last item — will be at index 5.

If, at this point, we are bringing a damselfish to the aquarium and we wanted to maintain alphabetical order based on the list above, we would put the item at index 3: `fish.insert(3,'damselfish')`.

##### list.count()

`list.count()` method will return the number of times the value x occurs within a specified list. This is useful for when you want to search a large list for the frequency of an item in a list. Say that you have a list of employees salaries and you would like to know how many people have the same salary as you: `20000`. You could use could to help with this situation.
```python
salaries = [20000, 45000, 90000, 70000, 20000, 90000]
print(salaries.count(20000))
```
Output: `2`

Because the number 20000 occurs twice, the number 2 is returned.

##### list.sort()

We can use the `list.sort()` method to sort the items in a list.

Just like `list.count()`, `list.sort()` can make it more apparent how many of a certain integer value we have, and it can also put an unsorted list of numbers into numeric order.

Let's use the integer list, `fish_ages` to see the `.sort()` method in action:
```python
fish_ages = [1,2,4,3,2,1,1,2]
fish_ages.sort()
print(fish_ages)
```
Output: `[1, 1, 1, 2, 2, 2, 3, 4]`

By using `.sort()` with `fish_ages`, the integer values are returned in order.
In practice, since these ages correspond to specific fish, you would likely want to make a copy of the original list prior to sorting it.

We can sort a list in reverse order by using the optional parameter `reverse`. The default value for the parameter is `False`.

Sorting a list in reverse
```python
fish_ages = [1,2,4,3,2,1,1,2]
fish_ages.sort(reverse=True)
print(fish_ages)
```
Output: `[4, 3, 2, 2, 2, 1, 1, 1]`

##### list.remove()

We can use the `list.remove()` method to remove an item in a list.

Removing Cod From list
```python
fish = ["barracuda", "cod", "devil ray", "eel"]
fish.remove("cod")
print(fish)
```
Output:
```
['barracuda', 'devil ray', 'eel']
```
Applying your knowledge

1. Create a `list` of strings called `my_friends`. Fill this list with the following names: "Rizzo", "French", "Danny", "Kenickie", "Marty", "Sandy", "Cha-Cha", "Patty", "Sonny", "Calhoun"
    
2. Use your `my_friends` list for the following:
    
    
    1. print out the length of the list
        
    2. print out the 4th friend's name
        
    3. print out the 11th friend's name (What happens?)
        
        
        1. once you have run this once, comment out the above line
            
        
    4. print out the last friend's name (Use negative indexing)
        
    5. print out the 5th - 8th friend's names
        
    6. print out the last 5 names (Do not place a number in **both** start and stop)
        
    7. print out the first 3 names (Do not place a number in **both** start and stop)
        
    8. print out every other name, starting at the first name
        
    9. print out every third name, starting at the last name going backwards to the front of the list.
        
    10. change the 8th friend's name to "Elizabeth". Print out the changed list.
        
    11. add a new friend, `Danny`, to the end of the list. Print out the changed list.
        
    12. remove the 7th friend's name (They ate the last cookie in the jar). Print out the changed list.
        
    13. insert a new friend, `Sandy`, in the 3rd spot of the list. Print out the changed list.
        
    14. print out the number of times the name `Sandy` appears in the list.
        
    15. sort the list to be in alphabetical order. Print out the sorted list.
        
## Tuples

A **tuple** is a data structure in Python that is an **immutable**, or unchangeable, ordered sequence of elements. Because it is immutable, the elements in the tuple cannot be changed. The immutability of a tuple helps send the message to others that the information inside of the tuple should not change.

Each element or value that is inside of a tuple is called an item. Just as lists are defined as items between square brackets, tuples are defined by having values between parenthesis `( )` and separated by commas. Empty tuples look like: `grade_level = ()`, but even tuples with just one item must use commas as in `grade_level = (9, )`

A tuple in Python looks like:
```python
emp_rank = ("Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal")
```
If we were to print the above tuple, it would look like the following:
```python
print(emp_rank)
```
Output: `("Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal")`

### Length

`len()`, just like in a string or a list, allows you to find the number of elements that are in a tuple. Do the following to find the length of a tuple:
```python
emp_rank = ("Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal")
print(len(emp_rank))
```
Output: `4`


Keep in mind that length starts counting at 1


### Indexing

Just like a string or list, tuple's elements can be accessed individually with indexing.

For the `emp_rank` tuple, the index break down looks like:

| Software Engineer | Sr. Software Engineer | Staff Software Engineer | Software Engineer Principal |
| :---: | :---: | :---: | :---: |
| 0 | 1 | 2 | 3 |

The first item `Software Engineer` starts at index 0, and the list ends at index 3 with `Software Engineer Principal`

Accessing the first item in the tuple emp_rank
```python
print(emp_rank[0])
```
Output: `Software Engineer`

Similar to strings and lists, be careful to not go out of bounds. In the `emp_rank` tuple, any number greater than 3 would give an `IndexError`. Negative numbers are valid inputs for indexes. The negative breakdown of `emp_rank` is:

| Software Engineer | Sr. Software Engineer | Staff Software Engineer | Software Engineer Principal |
| --- | --- | --- | --- |
| -4 | -3 | -2 | -1 |

We can concatenate string items in a tuple with other strings using the `+` operator:
```python
print('The current employee has the position of ' + emp_rank[2])
```
Output: `The current employee has the position of Sr. Software Engineer`

### Slicing

Similar to lists and strings, you can access part of a tuple with slicing with a range of index numbers separated by a colon `[x: y]`.

Printing the middle part of the emp_rank tuple
```python
print(emp_rank[1: 3])
```
Output: `("Sr. Software Engineer", "Staff Software Engineer")`

Leaving out either the start or stop range when slicing means you either want to start at the beginning of the tuple or go to the end of a tuple.

Printing from the beginning of the tuple up to, but not including, index 3
```python
print(emp_rank[: 3])
```
Output: `("Software Engineer", "Sr. Software Engineer", "Staff Software Engineer")`

Printing from index 3 up to the end of the tuple
```python
print(emp_rank[3: ])
```
Output: `("Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal")`

One last thing that we can use with slicing is the **step**. Step is how many items to move forward after the first item is retrieved from the tuple. Before this point with tuples, we have not used the step parameter, meaning we are using the default step value of one.

This syntax for this construction is `tuple[x: y: z]`, with z referring to stride. Let's make a larger tuple, then slice it, and give the step a value of 2:
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[1: 9: 2])
```
Output: `(1, 3, 5, 7)`

The above example starts at index 1, goes up to (but not including) 11, going up by 2's (every other item).

We can omit the first two parameters and use step alone with the syntax `tuples[: : 2]`
```python
print(numbers[: : 3])
```
Output: `(0, 3, 6, 9)`

We can print the tuple backwards with a negative step
```python
print(numbers[: : -2])
```
Output: `(10, 8, 6, 4, 2, 0)`

### Concatenating

Operators can be used to concatenating We'll look at using the `+` and \* operators and their compound forms `+=` and `*=`

The `+` operator can be used to concatenate two or more lists together:
```python
first_names = ("Noelle", "Tereza", "Raelin", "Linus")
last_names = ("Blossom", "Chrissy", "Grover", "Devin")
print(first_names + last_names)
```
Output: `("Noelle", "Tereza", "Raelin", "Linus", "Blossom", "Chrissy", "Grover", "Devin")`

### Tuples vs. Lists

The main way that tuples are different from lists is the fact that they are immutable, unable to be changed. This means that items cannot be changed, added or removed from a tuple, whereas a list item can do all of those.

Considering the `emp_rank` tuple:
```python
emp_rank = ("Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal")
```
Say we want to replace the item "Software Engineer" with a different item called "Newbie Software Engineer". If we try to change that output the same way we do a list, by typing:
```python
emp_rank[0] = "Newbie Software Engineer"
```
We would receive the error: `TypeError: 'tuple object does not support item assignment'`

This is because tuples cannot be modified. If we create a tuple and decide what we really need is a list, we can convert it to a list. To convert a tuple to a list, we can do so with `list()`.
```python
list(emp_rank)
```
This changed our tuple to a list:
```python
print(emp_rank)
```
Output: `["Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal"]`

### Applying your knowledge

1. Create a tuple called `vowels` that stores all of the vowels of the alphabet: a, e, i, o, u
    
2. Using `vowels`, do the following:
    
    
    1. Print out the length of the `vowels`
        
    2. Print out the 3rd vowel in `vowels`
        
    3. Print out the 1st - 4th vowel (Use both the start and stop)
        
    4. Print out the 1st - 4th vowel (Do not use **both** the start and stop)
        
    5. Print out e and o using slicing
        
    6. Change the last vowel to `y`. What happens?
        
        
        1. After you are done with the above step, comment it out
            
        
    

* * *

## Sets

A **set** is a mutable data structure in Python that contains an unordered collection of elements. These elements are unique (no repeats) and unordered. Sets are used for removing duplicate entries and performing set operations such as intersection, union and difference.

There are two built-in set types: set and frozenset. The set type is mutable and the frozenset type is immutable.

Set Ups of a Set

- `set()` for an empty set.
    
- `set(values)`
    
- `{value1, valuen}`
    

Creating a `frozenset` is very similar and uses `frozenset()` instead of `set()`.

Example of an Empty Set
```python
myset1 = set()
print(myset1)
```
Output: `set()`

When a set is given a string or any other iterable, it return a set composed of the iterable's elements.

Example of a Set with a String
```python
myset = set('aabbbbc')
print(myset)
```
Output: `{'b', 'a', 'c'}`

Example of a Set with a List
```python
positions = set(["Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal", "Software Engineer"])
print(positions)
```
Output: `{'Sr. Software Engineer', 'Software Engineer', 'Staff Software Engineer', 'Software Engineer Principal'}`

Example of `{ }` Syntax
```python
languages={'python','java','c#','php'}
print(languages)
```
Output: `{'c#', 'php', 'java', 'python'}`

### Length

`len()`, just like in a string, tuple or a list, allows you to find the number of elements that are in a set. Do the following to find the length of a set:
```python
positions = set(["Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal", "Software Engineer"])
print(len(positions))
```
Output: `4`

### Set Methods

Set has several **methods** that are very helpful. We are going to briefly cover some of the set methods that are available.

**Intersection**

The method `set1.intersection(set2)` will find the similar elements in both set1 and set2.

![set intersection](../images/set-intersection.jpg)

Example of finding the similar favorite programming languages of Jo and Al
```python
jos_favs = {'python', 'c++', 'javascript'}
als_favs = {'c#', 'python'}
print(jos_favs.intersection(als_favs))
```
Output: `{'python'}`

**Difference**

The method `set1.difference(set2)` will find the elements in set1 and set2 that are different.

![set difference]( ../images/set-difference.jpg)

Example of finding the different favorite programming languages of Jo and Al
```python
jos_favs = {'python', 'c++', 'javascript'}
als_favs = {'c#', 'python'}
print(jos_favs.difference(als_favs))
```
Output: `{'javascript', 'c++'}`

**Union**

The method `set1.union(set2)` will show the combination of elements in set1 and set2.

![set union]( ../images/set-union.jpg)

Example of showing the combination of favorite programming languages of two people
```python
jos_favs = {'python', 'c++', 'javascript'}
als_favs = {'c#', 'python'}
print(jos_favs.union(als_favs))
```
Output: `{'python', 'javascript', 'c#', 'c++'}`

### Modifying Sets

Since sets are mutable, you can add, remove and modify elements after creation.

The following methods do not work with `frozensets`.

#### Adding

The method `set.add(x)` will modify the set to include `x`. If `x` is already in the set, there will not be a change.

Example of add method
```python
jos_favs = {'python', 'c++', 'javascript'}
jos_favs.add('java')
print(jos_favs)
```
Output: `{'python', 'java', 'javascript', 'c++'}`

#### Removing

The method `set.remove(x)` will modify the set to not include `x`. If x is not in the set, there will not be a change.

Example of remove method
```python
jos_favs = {'python', 'c++', 'javascript', 'java'}
jos_favs.remove('java')
print(jos_favs)
```
Output: `{'python', 'javascript', 'c++'}`

* * *

### Applying your knowledge

1. Create a set called `set1` with a string with a value of `aaabcccccdd` (Use the `set()` notation). Print out the values of the set after you create it
    
2. Create a set called `set2` with a string with a value of `"b", "a", "t", "s", "c", "a", "t", "s"` (Use the `{value1}` notation). Print out the values of the set after you create it
    
3. Print out the number of elements in set1
    
4. Print out what `set1` and `set2` have in common
    
5. Print out what values that `set1` has that `set2` does not have
    
6. Print out the combination of `set1` and `set2`
    
7. Add the letter `e` to `set1`. Print out the new set
    
8. Remove the letter `b` from `set2`. Print out the new set
    

## Dictionaries

If you want to look up a meaning of a word, you use a dictionary. Whether it is online or a book, you look up the word and the definition is returned! In this example, you could think of the word as a key and the definition as the value that is returned. A Python dictionary is a collection of key-value pairs, just like in a "regular" dictionary!

**Keys** in a dictionary must be unique. The key and value pairs are listed between curly brackets. Dictionaries are useful whenever you have items that you wish to link together and want to store results for a quick look up.

### Dictionary Set Up
```python
salaries = {'Pam': 12000, 'Jim': 10000, 'Dwight': 50000}
```
Dictionaries are surrounded by curly braces and each key and value pair are separated by a colon.

The keys in the above dictionary are `Pam`, `Jim` and `Dwight`.

The values are `12000`, `10000`, `50000`.

### Printing Dictionaries
```python
print(salaries)
```
Output: `{'Pam': 12000, 'Jim': 10000, 'Dwight': 50000}`

### Accessing Elements

When accessing specific key value pairs, we call the values by referencing the related keys. If we wanted to see Jim's salary, we could do so by calling `salaries['Jim']`.
```python
print(salaries['Jim'])
```
Output: `10000`

Dictionaries act like a database in that instead of calling an integer to get a particular index value as you would with a list, you assign a value to a key and can call that key to get its related value.

By invoking the key `Jim`, we receive the value of that key, which is `10000`.

### Methods to Access Elements

In addition to using keys to access values, we can also work with some built-in methods:

- `dict.keys()` lists off just the keys
    
- `dict.values()` lists off just the values
    
- `dict.items()` lists key-value pairs in a list format `(key, value)` tuple pairs.
    

For the example uses of the dictionary methods, we will use the following dictionary:
```python
results_10k = {'Elizabeth': '56: 09', 'Emily': '56: 23', 'Alison': '57: 36'}
```
To return the keys, we would use the `dict.keys()` method. In our example, that would use the variable name and by `results_10k.keys()`. This method printed would look like the following:
```python
print(results_10k.keys())
```
Output: `dict_keys(['Elizabeth', 'Emily', 'Alison'])`

We receive output that places the keys within an iterable view object of the `dict_keys` class. The keys are then printed within a list format.

Similarly, we can use the `dict.values()` method to query the values in the `results_10k` dictionary, which would be constructed as `results_10k.values()`. Let's print those out:
```python
results_10k = {'Elizabeth': '56: 09', 'Emily': '56: 23', 'Alison': '57: 36'}
print(results_10k.values())
```
Output: `dict_values(['56: 09', '56: 23', '57: 36'])`
Both the methods `keys()` and `values()` return unsorted lists of the keys and values present in the dictionary with the view object of dict_keys and dict_values respectively.

If you are interested in all of the items in a dictionary, we can access them with the `items()` method:
```python
print(results_10k.items())
```
Output: `dict_items(['Elizabeth': '56: 09', 'Emily': '56: 23', 'Alison': '57: 36'])`
The returned format of this is a list made up of `(key, value)` tuple pairs with the dict_items view object.

### Modifying Dictionaries

Dictionaries are mutable, meaning they can have items changed, removed, or added.

#### Adding

Without using a method, you can add key-value pairs to dictionaries by using the following syntax:
```
dict[key] = value
```
We will look at how this works in practice by adding a key-value pair to our results_10k dictionary:
```python
results_10k['Laurel'] = '59: 40'
print(results_10k)
```
Output: `{'Elizabeth': '56: 09', 'Emily': '56: 23', 'Alison': '57: 36', 'Laurel': '59: 40'}`
The above output shows that the new `'Laurel': '59: 40'` has been added to the dictionary. Because dictionaries may be unordered, this pair may occur anywhere in the dictionary output. If we use the `results_10k` dictionary later in our program file, it will include the additional key-value pair.

#### Modifying Existing Items

This same syntax is used if you want to update an already existing value for a key. Let's consider 'Alison', if we made a mistake in showing her time and needed to update it, we could simply type: `results_10k['Alison']`. Now if you were to print the `results_10k` dictionary, you would get the following result:
```python
results_10k['Alison'] = '55: 36'
print(results_10k)
```
Output: `{'Elizabeth': '56: 09', 'Emily': '56: 23', 'Alison': '55: 36', 'Laurel': '59: 40'}`

#### Deleting

Just as you can add key-value pairs and change values within the dictionary data type, you can also delete items within a dictionary.

To remove a key-value pair from a dictionary, we'll use the following syntax:
```
del dict[key]
```
Let's take the `results_10k` dictionary and say that Laurel does not want her results to be displayed any more. To remove her time, we would do the following:
```python
results_10k = {'Elizabeth': '56: 09', 'Emily': '56: 23', 'Alison': '55: 36', 'Laurel': '59: 40'}
del results_10k['Laurel']
print(results_10k)
```
Output: `{'Elizabeth': '56: 09', 'Emily': '56: 23', 'Alison': '55: 36'}`

The line `del results_10k['Laurel']` removes the key-value pair `'Laurel': '59: 40'`

* * *

### Applying your knowledge

1. Create a dictionary called `cool_ranking`. Set the corresponding keys equal to their values: "Chandler" = 1, "Monica" = 10, "Ross" = 5, "Phoebe" = 2, "Joey" = 3, "Rachel" = 4.
    
2. Use the `cool_ranking` for the following:
    
    
    1. print out the ranking of 'Monica'
        
    2. add the following key-value pair to the dictionary: 'Janice' = 6. Print out the new dictionary
        
    3. print out all of the keys of the dictionary
        
    4. print out all of the values of the dictionary
        
    5. print out all of the key, value pairs of the dictionary in a list format.
        
    6. change 'Monica' to have a ranking of 7. Print out the new dictionary.
        
    7. remove 'Janice' from the dictionary. Print out the new dictionary.
        
## NoneType

Let's create a dictionary to explain the `NoneType`.
```python
groceries =
{
    "ribeye steak":  4,
    "russet potatoes":  "2 lbs",
    "coleslaw":  None,
    "corn on the cob":  "4 ears",
    "pork ribs":  "3 lbs"
}
```
We've never seen what `"coleslaw"` is set to. It says `None` and within the console, you can see the value `NoneType` for the key `"coleslaw"`.

This means we've told Python to **specifically** interpret the value for `"coleslaw"` as null, or empty. Python has a `NoneType` object it slaps on keys which technically don't yet have a value. We have to make sure to **tell** it not to have value, by using the word `None`.

Python will interpret the value of `coleslaw` as `None` until we intentionally set a value to `coleslaw`
