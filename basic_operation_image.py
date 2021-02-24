import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
# img2 = cv2.imread('0a3UtNzl5Ll3sq8K.png')

# print(img.shape)
# print(img.size)
# print(img.dtype)
# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))

# img = cv2.resize(img,(512,512))
# img2 = cv2.resize(img2,(512,512))
print(img.shape)
plt.imshow(np.asarray(img))
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()