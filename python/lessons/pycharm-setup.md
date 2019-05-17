---
title: "pycharm-setup"
type: "lesson"
---

# PyCharm Setup

## Getting Started

We installed Python3 onto every iMac for this class. For your personal computer, you'll want to visit the [Python website](https://www.python.org/downloads/) to download the newest version of Python.

PyCharm is an Integrated Development Environment used in computer programming, specifically for the Python language. Here at Home Depot, we have a dedicated license to use PyCharm Professional, Community and Edu versions. Just download the [JetBrains Toolbox](https://www.jetbrains.com/toolbox/) on **bandsaw** wifi and you can have PyCharm and more on your own machine.

## Configuring Python Interpreters

To access the interpreter settings:

- Go to PyCharm in the menu bar and click `PyCharm > Preferences` and then click the link for `project interpreter`
    
- Click the gear to the right of the Project Interpreter input. **Click `Add`**
    
- Click the radio button labeled `Existing environment`
    
- Click the three dots to the right of the `Interpreter` input.
    
- Choose this file path on your Mac: `/usr/local/bin/python3`
    
- Check off **Make available to all projects**
    
- Click `OK`
    
- On the current window, you should see the path you chose in the `Project Interpreter` dropdown. You may also see a list of packages, including `pip`
    
- Click `Apply` and `OK`
    

## Installing Packages

Make sure you're in the `Project Interpreter` preferences panel.

Click the `+` on the lower left hand corner of the packages list.

Search for the packages you need to use for your project.

Click `Install Package` in the lower left hand corner of the window.

Click the red dot in the upper left hand corner of the window to close it, you should see your new package in the list on the following screen.

Click `Apply`.

## Connecting Project to GitHub

For this section, make sure you're on the **bandsaw** wifi network.

[Connecting PyCharm and GitHub](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html)

- Log in to your Home Depot GitHub account at: [GitHub at Home Depot](https://github.homedepot.com)
    

* * *

- Open PyCharm to create repository on GitHub
    
    
    - Go to **Preferences**
        
    - Select **`Version Control | GitHub`**
        
    - Select **Password** authentication
        
    - Click the dropdown on the right hand side and select `Login`
        
    - Type `github.homedepot.com` into the `Host` field
        
    - Type your LDAP into the `Login` field
        
    - Type your password into the `Password` field
        
    

* * *

- Create a new project in PyCharm
    
    
    - Open PyCharm and create a project called `PythonFoundations`
        
    - Click `VSC` \> `Import Into Version Control` \> `Share Project on GitHub`
        
    - Type in a description in the description box.
        
    - Make sure that all boxes are checked
        
    - Click `OK`
        
    - In the box that says `Remember, don't ask again`
        
    - Click `Yes`
        
    

* * *

- Every time you'd like to push new changes to this GitHub repository do the following:
    
    
    - Go to `VCS` in the menu bar
        
    - Click `Git` \> `Commit File`
        
    - Check off all files you'd like to commit
        
    - Click `Commit`
        
    - Click `Push`
        
    

## Creating a default template for PyCharm

- Go to `File` \> `Default Settings`
    
- Click on `Editor` \> `File and Code Templates`
    
- Click on `Python Script`
    
- Type the following into the text box
    
```
"""
title: ${NAME}
author: ${USER}
date: ${DATE} ${TIME}
"""
```

## Adding a GitHub repository to PyCharm

- Clone your existing GiHub repository by clicking the green `Clone or Download` button and copying the URL (The URL should start with `https` and end with `.git`)
    
- Open PyCharm and go to `VCS > Check Out From Version Control > Git`
    
- Paste your GitHub repository URL in the space provided and click `clone`
    
