import cv2
import numpy as np

img = cv2.imread('gradient.png',0)
_, th1 = cv2.threadshold(img, 127,255, cv2.THRESH_BINARY)

cv2.imshow("Image",img)
cv2.imshow("th1",th1)

cv2.waitKey(0)
cv2.destroyAllWindows()