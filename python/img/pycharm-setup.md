# PyCharm

For the majority of this course we'll be using PyCharm. PyCharm was created specifically for Python development much like IDLE and it has some nice features. Python tends to be very opinionated around indentation and other syntax, and PyCharm will raise these errors for us before we even run the program! This helps with creating good habits around writing Python right off the bat.

# Getting Started

We installed Python3 onto every iMac for this class. For your personal computer, you’ll want to visit the [Python website](https://www.python.org/downloads/) to download the newest version of Python.

PyCharm is an Integrated Development Environment used in computer programming, specifically for the Python language. Here at Home Depot, we have a dedicated license to use PyCharm Professional, Community and Edu versions. Just download the [JetBrains Toolbox](https://www.jetbrains.com/toolbox/) and you can have PyCharm and more on your own machine.

# Configuring Python Interpreters

To access the interpreter settings:

* Go to PyCharm in the menu bar and click `PyCharm > Preferences` and then click the link for `project interpreter`
* Click the gear to the right of the Project Interpreter input. **Click `Add`**
* Click the radio button labeled `Existing environment`
* Click the three dots to the right of the `Interpreter` input.
* Choose this file path on your Mac: `/usr/local/bin/python3`
* Check off **Make available to all projects**
* Click `OK`
* On the current window, you should see the path you chose in the `Project Interpreter` dropdown. You may also see a list of packages, including `pip`
* Click `Apply` and `OK`
    

## Connecting Project to GitHub

[Connecting PyCharm and GitHub](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html)

* Log in to your GitHub account at: [GitHub](https://github.com)
    
---

* Open PyCharm to create repository on GitHub
    * Go to **Preferences**    
    * Select **Version Control | GitHub**    
    * Select **Password** authentication     
    * Click the dropdown on the right hand side and select `Login`     
    * Type `github.homedepot.com` into the `Host` field      
    * Type your LDAP into the `Login` field      
    * Type your password into the `Password` field

---

* Create a new project in PyCharm
    * Open PyCharm and click `Create New Project`. 
    * Change Location: `/Users/omstudent/OrangeMethodHighSchool`. Expand `Project Interpreter: New Pipenv environment`
        * 
    * Click `VSC` \> `Import Into Version Control` \> `Share Project on GitHub`   
    * Type in a description in the description box.
    * Make sure that all boxes are checked
    * Click `OK`
    * In the box that says `Remember, don't ask again`
    * Click `Yes`
        

## Creating a default template for PyCharm

* Go to `File` \> `Default Settings`
* Click on `Editor` \> `File and Code Templates`
* Click on `Python Script`
* Type the following into the text box
    
```
"""
title: ${NAME}
author: ${USER}
date: ${DATE} ${TIME}
"""
```
