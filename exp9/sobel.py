import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('nature.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (3,3), 0)
sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)

sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

sobel_combined = cv2.magnitude(sobelx, sobely)

plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel - X (Vertical edges)')

plt.subplot(1,3,2)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel - Y (Horizontal edges)')

plt.subplot(1,3,3)
plt.imshow(sobel_combined, cmap='gray')
plt.title('Combined Sobel Edge Detection')

plt.show()
