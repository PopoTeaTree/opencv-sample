import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')



titles = ['image','2D Convolution']
images = [img,dst]

for i in range(1):
    plt.subplot(1 ,1 , i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()