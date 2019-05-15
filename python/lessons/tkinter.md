---
title: "tkinter"
type: "lesson"
---
- [Tkinter](#tkinter)- [1\. Window Properties](#window_properties)- [1.1. Resizing](#resizing)
        - [1.2. Title](#title)
        
    - [2\. Geometry Management](#geometry_management)
    - [3\. Tkinter Widgets](#tkinter_widgets)- [3.1. Label](#label)
        - [3.2. Entry](#entry)
        - [3.3. Radiobutton](#radiobutton)
        - [3.4. tkMessageBox](#tkmessagebox)
        - [3.5. Button](#button)
        
    - [4\. Example Tkinter Program](#example_tkinter_program)
    

An introduction to the Tkinter library in Python

[Back to Python Foundation Workshop Guide](00-index.html)

# Tkinter

Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

Tkinter makes it to where creating a GUI application is an easy process. To create the "Hello World" of Tkinter you need to follow the following steps:

1. Import the `Tkinter` module.
    
2. Create the GUI application window
    
3. Enter the main event loop
    

from tkinter import *
root = Tk()
root.mainloop()

img/tkinter/tk-intro.png)

##Window Properties

### 1.1. Resizing

The `geometry()` method is used to resize the window by specifying the desired width and height in pixels.

from tkinter import *
root = Tk()
root.geometry("530x150")
root.mainloop()

resized window](img/tkinter/resized-window.png)

### 1.2. Title

The `title()` method is used to change the title of the window (what is stated at the top of the window).

from tkinter import *
root = Tk()
root.geometry("530x150")
root.title("Tkinter Tutorial")
root.mainloop()

titled window](img/tkinter/titled-window.png)

##Geometry Management

Tkinter windows have properties that have the purpose of organizing items on the window. Tkinter has three geometry manager classes: `pack`, `grid`, and `place`. We are going to focus the `grid()` manager. In the `grid` manager, we can specify which row and column we want to put a widget.

Example of the breakdown of a window using the `grid()` Geometry Manager

![tkinter grid](img/tkinter/tkinter-grid.png)

##Tkinter Widgets

Tkinter provides various controls, such as buttons, labels and text boxes called **widgets** used in a GUI application. Each widget has a set of event handlers to allow for user interaction. Widgets are called before the `root.mainloop()` line.

There are currently 15 types of widgets in Tkinter. Some of the widgets are described below:

| Widget Name | Description |
| --- | --- |
| 

Label

 | 

Provides a single-line caption for other widgets. It can also contain images.

 |
| 

Entry

 | 

Displays a single-line text field for accepting values from a user.

 |
| 

Radiobutton

 | 

Displays a number of options as radio buttons. The user can select only one option at a time.

 |
| 

Button

 | 

Displays the buttons in an application

 |
| 

tkMessageBox

 | 

Displays message boxes

 |

To explain the different widgets, we are going to go through an example application that is shown below.

![tkinter tutorial](img/tkinter/tkinter-tutorial.png)

### 3.1. Label

In row 0, column 2, there is a Label widget that says `Tkinter Widget Lesson`.

Label Set Up

Label(window, text="what you want the label to say", font="font font_size font_style")
Label Example

title_label = Label(root, text="Tkinter Widget Lesson", font="Helvetica 12 bold")
title_label.grid(row=0, column=2)

Entry

The Entry widget is covering row 1, columns 1, 2, and 3. `columnspan` details how many columns the widget spreads across. To specify how wide you want the Entry widget to be, you use the `width` attribute, which represents how many characters could fit.

Entry Set Up

Entry(window)
Entry Example

name_entry = Entry(root, width=40)
name_entry.grid(row=1, column=1, columnspan=3)

If we wanted to have a default value inside of the Entry widget we would use `insert()`. This would give a value in the widget when the application first is pulled up, but it is still possible for the user to change the value.

insert Set Up

insert(location_of_text, text)
Entry using Default Value

name_entry = Entry(root, width=40)
name_entry.insert(END, "Jane Doe")
name_entry.grid(row=1, column=1, columnspan=3)

Default Entry](img/tkinter/entry-default-value.png)

If we wanted to print out the value that the user types in the Entry box, we would need to use `get()`.

print(name_entry.get())
Radiobutton

In rows 5 - 9, column 1, there are radio buttons. Radio buttons only allow for the user to select one option at a time. There are more steps than the previous widgets to set up a radio button.

1. Create a list with the options
    
2. Create a list that will hold each individual radio button
    
3. Create a variable that will store the selected value
    
4. Create a for loop that will:
    
    
    1. create each radio button with each option
        
    2. place the new radiobutton in the list of radio buttons
        
    3. place the new radiobutton on the window
        
    

Radiobuttons Example

sizes_choices = ["S", "M", "L", "XL", "XXL"]
sizes_radios = []
data = StringVar()
for i, option in enumerate(sizes_choices):
    curr_button = Radiobutton(root, text=str(option), variable=data, value=i)
    sizes_radios += [curr_button]
    sizes_radios[i].grid(row=i + 5, column=1, sticky=W)

tkMessageBox

`tkMessageBox` module is used to display message boxes in applications. This widget provides a number of functions that you can use to display an appropriate message. Two examples of uses are `showinfo()` and `showerror()`.

tkMessageBox Set Up

messagebox.use(title, message)
tkMessageBox Example

messagebox.showinfo("Welcome!", "Successfully Registered for the Race!")

tkmessagewindow](img/tkinter/tkmessagewindow.png)

### 3.5. Button

In row 10, column 3, there is a Button widget that says `Submit`. In this example, this is the first widget that we have that is using an **event handler**. A button event handler takes care of what to do (which function to call) when a user clicks on the button.

Button Set Up

Button(window, text="what you want the label to say", command=function to call)
Say there is a function `greeting`:

def greeting():
    messagebox.showinfo("Welcome!", "Successfully Registered for the Race!")

If you want to have a Button that will call the `greeting` function when clicked, you would write it in the following way:

submit_button = Button(root, text="Submit", command=greeting)
submit_button.grid(row=10, column=3)

If we changed `greeting` to have parameters, like the following:

def greeting(name):
    messagebox.showinfo("Welcome!", name + " You have successfully registered for the race!")

You would need to change the button command argument to use **lambda**. (We are not going to get into lambda details right now).

name = name_entry.get()
submit_button = Button(root, text="Submit", command=lambda: greeting(name))
submit_button.grid(row=10, column=3)

Example Tkinter Program

The complete code to create the above application is here:

from tkinter import *
from tkinter import messagebox

def main_window(root):
    title_label = Label(root, text="Tkinter Widget Lesson", font="Helvetica 12 bold")
    title_label.grid(pady=5, row=0, column=2, sticky=W)

    name_label = Label(root, text="Enter Name", font=("Helvetica", 12))
    name_label.grid(padx=5, row=1, column=0, sticky=E)

    age_label = Label(root, text="Enter Age", font=("Helvetica", 12))
    age_label.grid(padx=5, row=2, column=0, sticky=E)

    tshirt_label = Label(root, text="T-shirt Size", font=("Helvetica", 12))
    tshirt_label.grid(padx=5, row=4, column=0, sticky=E, pady=5)

    name_entry = Entry(root, width=40)
    name_entry.insert(END, "Jane Doe")
    name_entry.grid(row=1, column=1, columnspan=3)

    age_entry = Entry(root, width=40)
    age_entry.grid(row=2, column=1, columnspan=3)

    sizes_radios = []
    sizes_choices = ["S", "M", "L", "XL", "XXL"]
    data = StringVar()
    for i, option in enumerate(sizes_choices):
        curr_button = Radiobutton(root, text=str(option), variable=data, value=i)
        sizes_radios += [curr_button]
        sizes_radios[i].grid(row=i + 5, column=1, sticky=W)

    submit_button = Button(root, text="Submit", command=greeting)
    submit_button.grid(row=10, column=3, sticky=E)

def greeting():
    messagebox.showinfo("Welcome!", "Successfully Registered for the Race!")

if __name__ == "__main__":
    root = Tk()
    root.geometry("455x280")
    root.title("Tkinter Tutorial")
    main_window(root)
    root.mainloop()

```