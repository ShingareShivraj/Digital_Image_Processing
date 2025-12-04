import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.exposure import match_histograms

img1 = cv2.imread('car.jpg')
img2b = cv2.imread('nature.png')
img2 = cv2.resize(img2b, (img1.shape[1], img1.shape[0]))
matched = match_histograms(img1, img2, channel_axis=-1)

res = np.hstack((img1, img2, matched))
cv2.imshow('Histogram Matching', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
plt.hist(gray.ravel(), 256, [0,256])
plt.title("Before matching")
plt.show()
gray1 = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
plt.hist(gray1.ravel(), 256, [0,256])
plt.title("After Equalization")
plt.show()