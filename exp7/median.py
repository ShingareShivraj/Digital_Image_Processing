import cv2
import numpy as np

img = cv2.imread('image.png', 0)
m, n = img.shape

img_median = np.zeros([m, n])

for i in range(1, m-1):
    for j in range(1, n-1):
       
        neighbors = [
            img[i-1, j-1], img[i-1, j], img[i-1, j+1],
            img[i,   j-1], img[i,   j], img[i,   j+1],
            img[i+1, j-1], img[i+1, j], img[i+1, j+1]
        ]
        
        median_val = np.median(neighbors)
        
        img_median[i, j] = median_val

img_median = img_median.astype(np.uint8)

cv2.imwrite('median_filtered.png', img_median)
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.imshow('Median Filtered Image', img_median)
cv2.waitKey(0)
x=cv2.hconcat([img, img_median])
cv2.imshow('Comparison', x)
cv2.waitKey(0)
cv2.destroyAllWindows()
