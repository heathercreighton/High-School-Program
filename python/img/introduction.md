### PyCharm

For the majority of this course we’ll be using PyCharm. PyCharm was created specifically for Python development much like IDLE and it has some nice features. Python tends to be very opinionated around indentation and other syntax, and PyCharm will raise these errors for us before we even run the program! This helps with creating good habits around writing Python right off the bat.

#### Getting Started

We installed Python3 onto every iMac for this class. For your personal computer, you’ll want to visit the [Python website](https://www.python.org/downloads/) to download the newest version of Python.

PyCharm is an Integrated Development Environment used in computer programming, specifically for the Python language. Here at Home Depot, we have a dedicated license to use PyCharm Professional, Community and Edu versions. Just download the [JetBrains Toolbox](https://www.jetbrains.com/toolbox/) on **bandsaw** wifi and you can have PyCharm and more on your own machine.

#### Configuring Python Interpreters

To access the interpreter settings:

* Go to PyCharm in the menu bar and click `PyCharm` > `Preferences` and then click the link for `project interpreter`
  
* Click the gear to the right of the Project Interpreter input. **Click `Add`**
  
* Click the radio button labeled `Existing environment`
  
* Click the three dots to the right of the `Interpreter` input.
  
* Choose this file path on your Mac: `/usr/local/bin/python3`
  
* Check off **Make available to all projects**
  
* Click `OK`
  
* On the current window, you should see the path you chose in the `Project Interpreter` dropdown. You may also see a list of packages, including `pip`
  
* Click `Apply` and `OK`
  

#### Installing Packages

Make sure you’re in the `Project Interpreter` preferences panel.

Click the `+` on the lower left hand corner of the packages list.

Search for the packages you need to use for your project.

Click `Install Package` in the lower left hand corner of the window.

Click the red dot in the upper left hand corner of the window to close it, you should see your new package in the list on the following screen.

Click `Apply`.

#### Connecting Project to GitHub

For this section, make sure you’re on the **bandsaw** wifi network.

[Connecting PyCharm and GitHub](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html)

* Log in to your Home Depot GitHub account at: [GitHub at Home Depot](https://github.homedepot.com)
  

* * *

* Open PyCharm to create repository on GitHub
  
  
  * Go to **Preferences**
    
  * Select **Version Control | GitHub**
    
  * Select **Password** authentication
    
  * Click the dropdown on the right hand side and select `Login`
    
  * Type `github.homedepot.com` into the `Host` field
    
  * Type your LDAP into the `Login` field
    
  * Type your password into the `Password` field
    
  

* * *

* Create a new project in PyCharm
  
  
  * Open PyCharm and create a project called `PythonFoundations`
    
  * Click `VSC` \> `Import Into Version Control` \> `Share Project on GitHub`
    
  * Type in a description in the description box.
    
  * Make sure that all boxes are checked
    
  * Click `OK`
    
  * In the box that says `Remember, don’t ask again`
    
  * Click `Yes`
    
  

* * *

* Every time you’d like to push new changes to this GitHub repository do the following:
  
  
  * Go to `VCS` in the menu bar
    
  * Click `Git` \> `Commit File`
    
  * Check off all files you’d like to commit
    
  * Click `Commit`
    
  * Click `Push`
    
  

#### Creating a default template for PyCharm

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

#### Create a config file to store API keys

So that we’re not sharing our API keys with the world of GitHub, follow these instructions to store your API keys in a config file in PyCharm.

* Create a `config.py` file in your root PyCharm project folder
  
* Put `api\_key\_variable = "PASTE YOUR API KEY HERE"` inside `config.py`
  
* Create a `.gitignore` file in your root PyCharm project folder
  
* Put the text: `config.py` inside your `.gitignore` file. GitHub will ignore the `config.py` file and your API keys will stay hidden.
  
* `import config` into any python file you need to use your API key in and then set a variable referencing config, such as this: `api\_key = config.api\_key\_variable`
  
* Simply use your `api\_key` variable within that file where your program calls for your API key.
  

#### Adding a GitHub repository to PyCharm

* Clone your existing GiHub repository by clicking the green `Clone or Download` button and copying the URL (The URL should start with `https` and end with `.git`)
  
* Open PyCharm and go to `VCS > Check Out From Version Control > Git`
  
* Paste your GitHub repository URL in the space provided and click `clone`