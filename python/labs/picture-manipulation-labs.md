---
title: "picture-manipulation-labs"
type: "lab"
---
- [1\. Changing Views of Images](#changing_views_of_images)- [1.1. Showing Two Images](#showing_two_images)
    - [1.2. Showing Five Images](#showing_five_images)
    - [1.3. Zooming In](#zooming_in)
    
- [2\. Modifying Images](#modifying_images)- [2.1. Changing Pixels](#changing_pixels)
    - [2.2. Changing Pixels Based on Color](#changing_pixels_based_on_color)
    - [2.3. Challenge: Create your own filter](#challenge_create_your_own_filter)
    
- [3\. Creating an Image](#creating_an_image)- [3.1. Altering Images](#altering_images)
    - [3.2. Adding a Newly Created Image](#adding_a_newly_created_image)
    

**Picture Manipulation**

[Back to Python Foundation Workshop Guide](00-index.html)

##Changing Views of Images

Open your Python file called `changing _view.py` within PyCharm. Your file should look like the following:

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
fig.show()
plt.ioff()
plt.show()

Showing Two Images

In your `changing _view.py` file, replace lines 12 and 13 with the following 2 lines:

| 

Old Line

 | 

New line

 |
| 

fig, ax = plt.subplots(1, 1)
ax.imshow(img)
fig,  ax  = plt.subplots(1,  2)
ax[0].imshow(img)
Run the code to see the new output.

Modify the code to look like the following:

![THD](img/picture-manipulation/modifying_two_images.png)

### 1.2. Showing Five Images

Comment out the changes you made in `Showing Two Images`. Using a for loop, modify the code to look like the following:

![THD](img/picture-manipulation/modifying_five_images.png)

### 1.3. Zooming In

Comment out the changes you made in `Showing Five Images`. Replace all of the code in the `'''Set Up Image Output'''` section and replace it with:

fig, ax  = plt.subplots(1,  2)
ax[0].imshow(img)
ax[1].imshow(img)
ax[1].set_xlim(300, 665)
ax[1].set_ylim(470, 120)
Here we introduce two new methods: `set _xlim` and `set _ylim`

| Methods | Description |
| --- | --- |
| 

`set _xlim(xmin,xmax)`

 | 

Set lower and upper limits to x-axis

 |
| 

`set _ylim(ymin,ymax)`

 | 

Set lower and upper limits to y-axis. Notice the first number is larger than the first number.

 |

This allows us to zoom in to the specific range of an image.

![THD](img/orange-method.png)

Using the above image, zoom in to three different 10 pixel by 10 pixel regions. An example is shown below:

![THD](img/picture-manipulation/zoom_three.png)

##Modifying Images

### 2.1. Changing Pixels

Create a new file called `manipulate _images.py` inside of your `picture-manipulation` project. Place the following in the file:

import matplotlib.pyplot as plt
import os.path
import numpy as np

'''Read the Image Data'''
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'orange-method.png')
img = plt.imread(filename)
img.setflags(write=1)

'''Modify Image'''
height = (len(img))
width = (len(img[0]))
for row in range(100, 120):
  for column in range(50, 100):
    img[row][column] = [0, 0, 1]

'''Show Image '''
fig, ax = plt.subplots(1, 1)
ax.imshow(img)
plt.ioff()
plt.show()

Run your code.

Alter the code to place a black box covering the `M`.

### 2.2. Changing Pixels Based on Color

Comment out the following lines of code with a multi-line comment:

for row in range(100, 120):
  for column in range(50, 100):
    img[row][column] = [0, 0, 1]

Under your new comment, add the following:

for row in range(155):
  for column in range(width):
    if sum(img[row][column]) > 2:
      img[row][column] = [0, 0, 1]

Run your code. Change your code to change the color of only the orange box around the word `Method` to a color of your choice.

Example Output![THD](img/picture-manipulation/pixel_color_change.png)

For a list of RGB percentages, look here: [http://www.december.com/html/spec/colorpercompact.html](http://www.december.com/html/spec/colorpercompact.html)

### 2.3. Challenge: Create your own filter

Using the tactics from the previous activities, create a filter like black and white or sepia on the Orange Method image or an image of your choice. (It is best to use a .png file)

##Creating an Image

#### 3.1. Altering Images

So far we have modified already created images. We are now going to create our own image. [Download this File](python-files/picture-manipulation-starter/make_image.py). Modify the code to look like following:

![THD](img/picture-manipulation/make_image.png)

#### 3.2. Adding a Newly Created Image

Create a fourth image with a crazy design of your choice.

[Manipulating CSVs](24-csv-manipulation.html)