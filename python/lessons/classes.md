---
title: "classes"
type: "lesson"
---
One of the most important concepts in object-oriented programming is the distinction between classes and objects, which are defined as follows:

- **Class** \- A blueprint created by a programmer for an object. This defines a set of attributes that will characterize any object that is instantiated from this class.
    
- **Object** \- An instance of a class. This is an **actual** occurrence of the class.
    

## Creating Classes

Classes are like a blueprint or a prototype that you can define to use to create objects. We define classes by using the `class` keyword, similar to how we define functions by using the `def` keyword.

**Class Set Up**
```python
class ClassName:
  """
  Optional class documentation string
  """
```
The class has a documentation string, which can be accessed via `print(ClassName.__doc__)` 

**Player Class**
```python
class Player:
    """
    Creates a game Player template.
    """

    def gain_point(self, points):
        """Prints that the user has gained a certain number of points."""
        print(f"Yay! You have gained {points} point(s)!")

    def lose_point(self, points):
        """Prints that the user has lost a certain number of points."""
        print(f"Oh no! You have lost {points} point(s)!")
```

Because these functions are indented under the class `Player`, ther are called methods. **Methods** are a special kind of function that are defined within a class.

The argument that both of these functions has is the word `self`, which is a reference to objects that are made based on this class. To reference instances (or objects) of the class, `self` will always be the first parameter, but it does not have to be the only one.

Defining this class did not create any `Player` objects, only the pattern for a `Player` object that we can define later. That is, if you run the program at this stage, nothing will be returned.

Creating the `Player` class above provided us with a blueprint for an object.

## Objects

An object is an instance of a class. We can take the `Player` class defined above, and use it to create an object or instance of it.

We will make a `Player` object called `ralph`:

```python
ralph = Player()
ralph.gain_point(10)
ralph.lose_point(5)
```
The `Player` object `ralph` is using the two methods `gain_point` and `lose_point`. We called these using the dot operator (`.`), which is used to reference an attribute of the object. In this case, the attribute is a method and it's called with parentheses, like how you would also call with a function.

Because the keyword `self` was a parameter of the methods as defined in the `Player` class, the `ralph` object gets passed to the methods. The `self` parameter makes sure that the methods have a way of referring to object attributes.

When we call the methods, the object `ralph` is being automatically passed with the dot operator.

**Player Class**

```python
class Player:
    """
    Creates a game Player template.
    """
    def gain_point(self, points):
        """Prints that the user has gained a certain number of points."""
        self.points += points
        print(f"Yay! You have gained {points} point(s)! That means you now have {self.points} points!")

    def lose_point(self, points):
        """Prints that the user has lost a certain number of points."""
        self.points -= points
        print(f"Oh no! You have lost {points} point(s)! That means you now have {self.points} points!")

def main():
  ralph = Player()
  ralph.gain_point(10)
  ralph.lose_point(5)

if __name__ == "__main__":
  main()
```
Output:
```
Yay! You have gained a 10 points!
Oh no! You have lost 5 points!
```

#### Constructor Methods

`init` is a special method in Python classes, it is the constructor method for a class. The constructor method is used to initialize data. It is run as soon as an object of a class is instantiated. The first parameter is always `self`. `self` is a special variable which points to the current object.

**Constructor in the Player class**

```python
class Player:
  def __init__(self):
    print("This is the constructor method")
```
If you added the above init method to the `Player` class in the program above, the program would output the following without your modifying anything within the `ralph` instantiation:

Output:
```
This is the constructor method.
Yay! You have gained a 10 points!
Oh no! You have lost 5 points!
```
This is because the constructor method is automatically initialized. You should use this method to carry out any initializing you would like to do with your class objects.

Instead of using the constructor method above, let's create one that uses a `points` variable that we can use to assign points to objects. We'll pass two parameters: `user _name` and `points` as a parameter with a default value of `0`. We will set `self.user _name` equal to `user _name` and `self.points` equal to `points`.


```python
class Player:
  def __init__(self, user_name, points=0):
    self.user_name = user_name
    self.points = points
```
Next, we can modify the strings in our functions to reference points, as below:

```python
class Player:
    """
    Creates a game Player template.
    """
    def __init__(self, user_name, points=0):
        self.user_name = user_name
        self.points = points

    def gain_point(self, points):
        """Prints that the user has gained a certain number of points."""
        self.points += points
        print(f"Yay {self.user_name}! You have gained {points} point(s)! That means you now have {self.points} points!")

    def lose_point(self, points):
        """Prints that the user has lost a certain number of points."""
        self.points -= points
        print(f"Oh no, {self.user_name}! You have lost {points} point(s)! That means you now have {self.points} points!")
```

Finally, we can set the user name to `"R@!ph123"` and the number of points a `Player` object `ralph` has to `10` by passing it as a parameter of the `Player` class.

```python
class Player:
    """
    Creates a game Player template.
    """
    def __init__(self, user_name, points=0):
        self.user_name = user_name
        self.points = points

    def gain_point(self, points):
        """Prints that the user has gained a certain number of points."""
        self.points += points
        print(f"Yay {self.user_name}! You have gained {points} point(s)! That means you now have {self.points} points!")

    def lose_point(self, points):
        """Prints that the user has lost a certain number of points."""
        self.points -= points
        print(f"Oh no, {self.user_name}! You have lost {points} point(s)! That means you now have {self.points} points!")

def main():
  ralph = Player("R@!ph123", 100)
  ralph.gain_point(10)
  ralph.lose_point(5)

if __name__ == "__main__":
  main()
```
Output:
```
Yay R@!ph123! You have gained a 10 points! That means you now have 110 points!
Oh no, R@!ph123! You have lost 5 points! That means you now have 105 points!
```

## Working with More Than One Object

Classes are useful because they allow us to create many similar objects based on the same blueprint.

To get a sense for how this works, let's add another `Player` object to our program:
```python
class Player:
    """
    Creates a game Player template.
    """
    def __init__(self, user_name, points=0):
        self.user_name = user_name
        self.points = points

    def gain_point(self, points):
        """Prints that the user has gained a certain number of points."""
        self.points += points
        print(f"Yay {self.user_name}! You have gained {points} point(s)! That means you now have {self.points} points!")

    def lose_point(self, points):
        """Prints that the user has lost a certain number of points."""
        self.points -= points
        print(f"Oh no, {self.user_name}! You have lost {points} point(s)! That means you now have {self.points} points!")

def main():
  ralph = Player("R@!ph123", 100)
  ralph.gain_point(10)
  sally = Player("iS@llee", 1245)
  sally.lose_point(5)

if __name__ == "__main__":
  main()
```
Output:
```
Yay R@!ph123! You have gained a 10 points! That means you now have 110 points!
Oh no, iS@llee! You have lost 1 points! That means you now have 1244 points!
```

#### Method Types

Example
```python
class Employee:
    """
    Creates the info for an Employee
    """
    emp_count = 0

    def __init__(self, name, ldap):
        self.name = name
        self.ldap = ldap
        Employee.emp_count += 1

    def display_employee(self):
        print (f"Name: {self.name}, LDAP: {self.ldap}")

    @classmethod
    def get_count(cls):
        return Employee.emp_count

    @staticmethod
    def take_home_salary(salary):
        return salary * 0.7
```

**Instance Methods**
```python
def display_employee(self):
    print (f"Name: {self.name}, LDAP: {self.ldap}")
```
Takes one parameter, `self`, which points to an instance of the class when the method is called.
    
- Can freely access attributes and other methods on the same object.
    
- Able to modify an object's class's state.
    
- Can access the class itself through the `self.class` attribute.
    

**Class Methods**
```python
@classmethod
def get_count(cls):
    return Employee.emp_count
```
Marked with a `@classmethod` decorator to flag it as a class method.
    
- Take a `cls` parameter that points to the class—and not the object instance—when the method is called.
    
- It can't modify object instance state. (That would require access to self.)
    
- It can still modify class state.
    

**Static Methods**

```python
@staticmethod
def take_home_salary(salary):
    return salary * 0.7
```
Marked with a `@staticmethod` decorator to flag it as a static method.
    
- Takes neither a `self` nor a `cls` parameter (but free to accept other parameters).
    
- It can neither modify object state nor class state.
    
- Static methods are restricted in what data they can access.
    

### Using Types of Methods
```python
if __name__ == "__main__":
    print("=================================")
    e1 = Employee("Hellen", 25000)
    e1.display_employee()
    print(f"Number of Employees: {Employee.get_count()}")
    print(f"Potential Salary: {Employee.take_home_salary(100)}")

    print("=================================")
    e2 = Employee("Jackson", 58000)
    e2.display_employee()
    print(f"Number of Employees: {Employee.get_count()}")
    print(f"Potential Salary: {Employee.take_home_salary(350)}")
```

**Key Points**

- Instance methods need a class instance and can access the instance through self.
    
- Class methods don't need a class instance. They can't access the instance (self) but they have access to the class itself via `cls`.
    
- Static methods don't have access to `cls` or `self`. They work like regular functions but belong to the class's namespace.
    