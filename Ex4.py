import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import imread

#1.1
img = imread("raccoon.jpg")
plt.imshow(img)
plt.show()

#1.2
ch0 = img[:,:,0] #r,g,b
ch1 = img[:,:,1] #r,g,b
ch2 = img[:,:,2] #r,g,b

#1.3
ch0 = np.fliplr(ch0) #reverse column
ch1 = np.flipud(ch1) #reverse row

#1.4
half = int(ch2.shape[1]/2.0) #horizontal
slice = slice(half, None, 3) #every third pixel
ch2[:,slice]= 255 - ch2[:,half::3] #255-pixel value in ch2

#1.5
img = np.stack([ch0, ch1, ch2], axis=2) #put togheter
plt.imshow(img)
plt.show()


