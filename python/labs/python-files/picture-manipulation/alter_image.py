import matplotlib.pyplot as plt
import os.path
import numpy as np

'''Read the Image Data'''
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'orange-method.png')
img = plt.imread(filename)
img.setflags(write=1)

'''Set Up Image Output'''
# link:picture-manipulation-labs.html#showing_two_images
'''
fig, ax = plt.subplots(1,  2)
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
'''

# link:picture-manipulation-labs.html#showing_five_images
'''
fig, ax = plt.subplots(1,  5)
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
'''
# link:picture-manipulation-labs.html#zooming_in

fig, ax = plt.subplots(1,  3)
ax[0].imshow(img)
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[0].set_xlim(90, 100)
ax[0].set_ylim(100, 90)
ax[1].set_xlim(100, 110)
ax[1].set_ylim(60, 50)
ax[2].set_xlim(150, 160)
ax[2].set_ylim(120, 110)

'''Show Image '''
fig.show()
plt.ioff()
plt.show()
