import matplotlib.pyplot as plt
import os.path
import numpy as np

'''Read the Image Data'''
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'orange-method.png')
img = plt.imread(filename)
img.setflags(write=1)

# link:picture-manipulation-labs.html#changing_pixels
'''Modify Image'''
height = (len(img))
width = (len(img[0]))
'''for row in range(99, 145):
  for column in range(18, 50):
    img[row][column] = [0, 0, 1]'''


# link:picture-manipulation-labs.html#changing_pixels_based_on_color

for row in range(90, 155):
  for column in range(width):
    if 1.3 < sum(img[row][column]) < 1.5:
      img[row][column] = [0, 0, 1]


'''Show Image '''
fig, ax = plt.subplots(1, 1)
ax.imshow(img)
plt.ioff()
plt.show()
