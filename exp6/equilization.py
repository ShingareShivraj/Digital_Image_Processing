import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('car.jpg', cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img1,(400,400))
equ = cv2.equalizeHist(img)

res = np.hstack((img, equ))

cv2.imshow('Equalization Result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(img.ravel(), 256, [0,256])
plt.title("Before Equalization")
plt.show()

plt.hist(equ.ravel(), 256, [0,256])
plt.title("After Equalization")
plt.show()
