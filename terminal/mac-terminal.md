# Terminal Commands

## Learning Objectives

* Introduction to Mac
* View the path of the current directory
* Navigate through the file system
* View the contents of a directory
* Create, copy, move, and delete files.
* Create, copy, move, and delete directories.
* Manage a file or directory’s ownership and permissions

## Intro to a Mac

### Mac keyboard shortcuts

| Name | Shortcut |
| --- | --- |
| Save File | `command` \+ `s`|
| Quit Program | `command` \+ `q` |
| Copy | `command` \+ `c`|
| Paste | `command` \+ `v` |
| Refresh browser window | `command` \+ `r`|
| Open Spotlight Search | `command` \+ `spacebar` |
| Force Quit | `command` \+ `option` \+ `escape` |

### Mac Commands

When you need to open a program on a Mac, simply type `command` \+ `spacebar` and the Spotlight Search bar will appear. Type the name of the program and press `return` to open it.

To save a file in a text editor such as VS Code, press `command` \+ `s` to save.

In order to quit a program, use `command` \+ `q`.

In the event a program has frozen, use the Force Quit option (similar to Control-Alt-Delete) which is `command` \+ `option` +`escape`.

To right click on the Mac’s mouse, let’s first open the System Preferences to view the default settings. Do `command` \+ `spacebar` and type `mouse` and hit `enter`

You can enable the two-finger right-click in these settings.

![Double Click](./images/double-click.png)
    
## File System

Your computer has a file system where all of your `files` are stored. These files are organized into `directories` (sometimes called `subdirectories` or `folders`).

This lesson is an introduction into the concepts and commands needed to manage the files and directories in your computer’s file system.

In this lesson we are focusing on UNIX based file systems which include the file systems you will encounter on MacOS, Linux, and other flavors of the UNIX operating system. While the Windows file system differs in some ways (particularly the file system management commands and the file and directory permissions), many of the concepts are similar.

### Types of Files

* text files
    * plain text
    * csv
    * html, xml, css, js, java, ruby
        
* binary files
    * documents: pdf
    * img: jpg, png, gif 
    * audio: mp3 
    * binary programs

### Directories

The file system is organized into a set of directories. Each of these directories can contain files or (sub) directories, forming a tree structure of parent, child, and grandchild directories, etc.

Example Directory Structure

```
.
└── Users
    ├── drmikeh
    │   ├── Applications
    │   │   └── Atom
    │   │   └── Chrome
    │   ├── Desktop
    │   │── Documents
    │   │   └── Resume.pages
    │   │   └── Resume.pdf
    │   ├── Music
    │   └── Pictures
    │       └── 2016
    │       │   └── pic1.jpg
    │       │   └── pic2.png
    │       │   └── pic3.gif
    │       └── 2017
    │       │   └── pic4.png
    │       │   └── pic5.png
    │       │   └── pic6.jpg
    │       └── 2018
    │       │   └── lol-cat1.jpg
    │       │   └── lol-cat2.jpg
    │       │   └── lol-cat3.jpg
    │       └── 2019
    └── Guest
        ├── Applications
        ├── Desktop
        ├── Documents
        ├── Music
        └── Pictures
```

### Paths

A path is a description of the location of a file or directory on our computer.

Our terminal (shell) is always working out of a single path at a time. Commands that are run will take action in the current path (directory) unless we tell them to do otherwise.

#### Relative vs Absolute Paths

All paths point to a single file or directory, but we can write paths to be either **relative** or **absolute**.

##### Absolute Paths

An absolute path will always tell us exactly where the file or directory is. An example in the real world would be a mailing address:

```
Store Support Center
2455 Paces Ferry Road
Atlanta, GA 30339
USA
Earth
Solar System
Milky Way
```

Absolute paths start with a `/` and go from top down (least specific to more specific):

```bash
/Milky_Way/Solar_System/Earth/USA/Atlanta/SSC
# or a realistic example
/Users/joehacker/orange-method/projects/project-2
```

The first slash essentially means "start at the root of the computer’s file system".

Some absolute paths instead start with a `~`. This is a shortcut to the absolute path of our home directory. So the above absolute path could also be written as

```
~/orange-method/fswd/projects/project-2
```

(assuming that you are `joehacker`).

##### Relative Paths

Relative paths are interpreted starting from the directory we’re in (aka the current working directory). They are similar to giving directions from a starting point, for example:

`Go to the end of the street, turn left, go to the 2nd light, turn right and it is the 3rd house on the left.`

The above directions only work from a specific starting point. It is the same with UNIX relative paths.

Relative paths start with anything but a slash `/` or a tilde `~`.

So if I were in my home directory, the path to my work directory could be written

```bash
orange-method/fswd                     # relative
~/orange-method/fswd                   # absolute
/users/joehacker/orange-method/fswd/   # absolute
```

If I were in a different directory, then the relative path would point to an entirely different directory/file.

Periods or dots are special in relative paths:

* One dot means "relative to the current directory"
    
* Two dots means "go up to the parent directory"
    

So if I’m in `~/orange-method/fswd` then the relative path `../personal\_projects` means "go up one level to the code directory, then down into personal\_projects".

We can use multiple `..` to go up multiple levels:

`../../Documents/top\_secret/lol\_cats/favorites/so\_many\_kittenz.jpg` would go up two levels, from `~/orange-method/fswd` to `~` (my home directory), and then down into my favorite lolcat picture.

#### Navigating The File System

From the terminal you will need to do the following:

* know your current working directory
* navigate to another directory
* create a new directory or file
* move or rename a directory or file
* copy a directory or file
* delete a directory or file
    
## Common Unix Commands

| Command | Description | Examples |
| --- | --- | --- |
| `pwd` | print the current working directory | `pwd` |
| `cd <path>` | change to a new directory | `cd` `cd ~/Downloads` `cd \\tmp` |
| `ls` | print a listing of the current directory | `ls`<br><br>`ls -a`<br><br>`ls -als \*.png`<br><br>`ls -alst ~/Downloads` |
| `touch file_name` | create a new file or update the timestamp of an existing file | `touch index.html`<br><br>`touch ~/projects/project3/app.js` |
| `cat` | print the contents of a file | `cat fruit.txt`<br><br>`cat ~/projects/project1/index.html` |
| `rm filename` | remove a file | `rm badfile.txt`<br><br>`rm ~/Downloads/monkey.jpg` |
| `cp source target` | copy the source file (or directory) to the target location (file or directory). | `cp monkey.png img/nice-monkey.png`<br><br>`cp ~/Downloads/banana.jpg ./img` |
| `mv source target` | move the source file (or directory) to the target location (file or directory). | `mv monkey.png img/nice-monkey.png`<br><br>`mv ~/Downloads/banana.jpg ./img` |
| `mkdir new-dir-name` | create a new directory | `mkdir project1`<br><br>`mkdir ~/project2` |
| `rmdir directory_name` | remove a directory | `rmdir project3`<br><br>`rmdir -r ~/projects/project3` |


You can use `Tab Completion` as you type to get auto-completion of your file and directory names. For instance if you are in a directory that contains a subdirectory named `Pictures`, you can type `cd Pic` and then press kbd:\$&tab\$& and the shell will complete your typing for you (unless there are 2 or more directories that begin with `Pic`, then you need to type enough characters to remove any ambiguity). Use `Tab Completion` a **lot** to work faster!


## Navigating to Your HOME Directory

Your `HOME` directory is associated with your login account. You can go to your `HOME` directory using any of the following commands:

```bash
cd               # no argument implies go to your HOME directory
cd $HOME         # $HOME refers to your HOME directory
cd ~             # in BASH the tilde symbol is a shortcut for your HOME directory
```

You can also use the `$HOME` or `~` shortcuts to navigate to a subdirectory under your `HOME` directory:

```bash
cd ~/Documents
cd ~/Pictures/2019
cd ~/fswd/projects/project2
```

## Looking Around

You can use the `ls` command to get a listing of the files and directories in your current working directory.

```bash
cd ~
ls       # show a simple listing
ls -F    # annotate the listing with extra characters that indicate the file types
ls -l    # show a long listing
ls -al   # show a long listing and include hidden files
```

## Activity

* https://github.com/elizabeth-phillips/kitchen-organizer


## Review

* Describe 4 BASH commands for managing directories and files.
    
* Write a command to list only files beginning with your first name and including the file ownership and permissions.
    
* You are currently in the "code" directory in the below file tree. How would you get to the directory that contains "beach.png" using the command line?
    

```
home
├── documents
│   └── code
├── photos
│   ├── headshot.jpg
│   └── summer_vacation_2018
│       └── beach.png
└── videos
```

