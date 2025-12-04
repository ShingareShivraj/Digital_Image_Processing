import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters

img = cv2.imread('nature.png', 0)

blur = cv2.GaussianBlur(img, (3,3), 0)

niblack_thresh = filters.threshold_niblack(blur, window_size=25, k=-0.2)
sauvola_thresh = filters.threshold_sauvola(blur, window_size=25, k=0.5, r=128)

binary_niblack = blur > niblack_thresh
binary_sauvola = blur > sauvola_thresh

titles = ['Original', 'Niblack Thresholding', 'Sauvola Thresholding']
images = [img, binary_niblack, binary_sauvola]

plt.figure(figsize=(10,6))
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
