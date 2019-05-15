---
title: "picture-manipulation"
type: "lesson"
---
- [1\. File Systems](#file_systems)- [1.1. Absolute File Paths](#absolute_file_paths)
    - [1.2. Relative File Paths](#relative_file_paths)
    
- [2\. RGB Percentages](#rgb_percentages)
- [3\. Numpy Arrays](#numpy_arrays)
- [4\. Rendering an Image](#rendering_an_image)- [4.1. Read the Image Data](#read_the_image_data)
    - [4.2. Image Set Up](#image_set_up)
    - [4.3. Set Up Image Output](#set_up_image_output)
    - [4.4. Figure](#figure)
    - [4.5. Showing the Image](#showing_the_image)
    

**Picture Manipulation**

[Back to Python Foundation Workshop Guide](unit-00-index.html)

Create a Python file called `picture _manipulation.py` within a PyCharm project called `python-fundamentals`

Have you ever played with special photo effects on a computer? In this lesson, we are going to talk about how those special effects are created.

##File Systems

Before talking about how to change an image, we need to figure out direct the program to the location of the file. To locate a file, there are two different ways to do so: **absolute** vs. **relative** file paths.

#### 1.1. Absolute File Paths

Most file systems are hierarchical, forming a **tree** that begins with a **root** directory. An absolute filename specifies where the file is stored from the root.

- In Windows, the root is typically indicated by the startup drive letter, such as `C:\`
    
- In Mac and Linux systems, the root is typically indicated by `/`
    

For example: the absolute file path of admin (in the green box below) is `C:\\Users\\admin`

![File Systems](img/picture-manipulation/file-systems.png)

### 1.2. Relative File Paths

Most operating systems and programming languages remember one location in the file system as your "present working directory". A file can be described relative to that location: a **relative file path**.

For example: In the above picture, the relative file path of `nice.jpg` from `admin` is `../Student login/Desktop/nice.jpg`. The two dots at the beginning represent "go up one directory".

##RGB Percentages

RGB represents red, green and blue light added together in various ways to reproduce a broad array of colors. An RGB color value is specified with three values: `[red, green, blue]`. Each parameter defines the intensity of the color as a floating point number between 0 and 1.

For example, \$&0, 0, 1\$& is rendered as blue, because the blue parameter is set to its highest value (`1`) and the others are set to `0`.

![Picture Manipulation](img/picture-manipulation/rgb-wheel.png)

##Numpy Arrays

Numpy is the core library for scientific computing in Python. We have talked about arrays and typed arrays before, a numpy array is a typed array and is indexed by a tuple of **positive** (non-negative) integers.

Before we can convert an image to a 3D **numpy array**, we would need to place the image in the current project that we are working on. Take the following image and save in your PyCharm project.

Arrays can be defined with items that are made up of arrays, with each bracketed array enclosed inside the larger brackets of the parent array. Say that we had an image that was a 2x3 pixel image. (2 rows and 3 columns) like the following:

![THD](img/picture-manipulation/numpy_array_demo.png)

We would create that with the following in Python:

import numpy as np
img = np.array([[[1, 0, 0], [1, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, 0, 0], [1, 0, 0]]])
print(img)
Output:

Rendering an Image

To render an image on a screen, we are going to use the Python library `matplotlib`. `matplotlib` is a Python 2D plotting library which allows you to create plots, histograms, bar charts, scatterplots, etc. The figures created by `matplotlib` are interactive **graphical user interfaces** (GUIs). To be able to manipulate the images, the images are converted into a **numpy array**.

### 4.1. Read the Image Data

Using the above numpy array, finding out the number of rows of the image is as follows:

Output:

print(len(img))
Output: `2`

To find out the number of columns of the image:
Output:

print(len(img[0]))
Output: `3`

From the table, it is visible that at position (0,1) is \$&1, 0, 0\$&. To access this same pixel in `img`, do the following:

print(img[0][1])
Output: `[1, 0, 0]`

If we wanted to change the bottom right pixel (`img\$&1\$&\$&2]`) to green (`[0, 1, 0]`), we would do the following:

print("Before: ", img[1][2], end="")
img[1][2] = [0, 1, 0]
print(" After: ", img[1][2])

Output: `Before: \$&1, 0, 0\$& After: \$&0, 1, 0]`

### 4.2. Image Set Up

You can copy and paste the image into the project by right clicking on the image and clicking copy, go into PyCharm and right click on the project name in PyCharm and click paste.

![THD](img/picture-manipulation/thd-vivid-orange.png)

**File Paths in Python**

When working with images in this lesson, we will be primarily using absolute file path. Since every user will save their projects/images in varying places, this allows the navigation to the project work on every computer. To get access to finding absolute paths in Python we are going to use the `os` library.

To work with file paths, we need to import the os module with the following:

import os
If we wanted to print the absolute file path of the current project in Python, we would do the following:

directory = os.path.dirname(os.path.abspath(__file__))
The above would set directory to a value with a value like the following:

Users/user123/PycharmProjects/python-fundamentals
If we had an image called `thd-vivid-orange.png` in the `python-fundamentals` folder, we would need to do the following to directly "point" at it.

filename  = os.path.join(directory, 'thd-vivid-orange.png')
The above would use the absolute path to the current directory that was receive with the `dirname` call and attach the file name, `thd-vivid-orange.png`, to the end.

**Convert to Numpy Array**

To work with numpy arrays, we need to import both `matplotlib` and `numpy` with the following:

import matplotlib.pyplot as plt
import numpy as np
When working with an image in matplotlib, you need to convert the image into a numpy array. To convert the image, use the following command:

img = plt.imread(filename)
File Permissions**

When working with an image, you need to make sure that you have permission to alter the image. In order to do this, you must change the image's "write" permission to allow this.

This is done with:

img.setflags(write=1)
Set Up Image Output

When working with image windows in matplotlib, you need to figure out how many images you want to show and where would you put them. The set up of images is in a grid format, so we will need to specify how many rows and columns that you need to show the desired images.

To create a 1x1 grid (1 row and 1 column) of images in a window, place the following line:

fig, ax = plt.subplots(1,1)
Software tools stretch the size of the image and generate pixels to fill in the blanks. **Interpolation** is the process by which a small image is made larger. Interpolated images produce smoother lines and a better large print than if the original, small image was simply printed large.

![THD](img/picture-manipulation/interpolation.png)

The default mode of an image in matplotlib is interpolated. To change `img` to not be interpolated and place the image in the 1x1 grid., use the following line of code:

ax.imshow(img, interpolation='none')
Objects and Methods**

A **class** is a category of **objects** that have **properties** (a set of variables with potentially unique values for each object) and **methods** (a common set of scripts that do things). An object is an **instance** of its class.

**Note:** We are not going to get too into this right now, just needed to show the terminology before we go over some examples.

From the above code:

| Code Snippet | Description |
| --- | --- |
| 

`fig, ax = plt.subplots(1,1)`

 | 

This line **returns** (gives back) a tuple that has two items in it:

- an **object** of the `Figure` which is being stored in a new variable, `fig`.
    
- an **object** of the `AxesSubplot` class which is being stored in the variable `ax`.
    

 |
| 

`ax.imshow(img, interpolation='none')`

 | 

The **method** is `imshow()` being called on the **object**`ax`. It is being given 1 argument: `img`.

 |

### 4.4. Figure

The whole figure. The figure keeps track of all the child Axes, artists (titles, figure legends, etc), and the canvas. A figure can have any number of Axes, but to be useful should have at least one.

![500](img/chart_figure/matplotlib_figure_anatomy.png)

| 

**Axes**

 | 

'a plot', it is the region of the image with the data space. The Axes class and it's member functions are the primary entry point to working with the OO interface.

 |
| 

**Axis**

 | 

These are the number-line-like objects. They take care of setting the graph limits and generating the ticks.

 |
| 

**Artist**

 | 

Basically everything you can see on the figure is an artist. This includes Figure, Axes, Axis, Text, Line2D, Collection, and Patch Objects.

When the figure is rendered, all of the artists are drawn to the canvas.

 |

### 4.5. Showing the Image

Place the following starter code in a new Python file called `changing _views.py`:

import matplotlib.pyplot as plt
import os.path
import numpy as np

'''Read the Image Data'''
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'thd-vivid-orange.png')
img = plt.imread(filename)
img.setflags(write=1)

'''Set Up Image Output'''
fig, ax = plt.subplots(1, 1)
ax.imshow(img, interpolation='none')

'''Show Image '''
plt.ioff()
plt.show()

Run your code and see the output.

[Picture Manipulation Lab](picture-manipulation-labs.html)