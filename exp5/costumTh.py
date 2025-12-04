import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('car.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

n = int(input("Enter number of threshold values: "))
lst = []
for i in range(n):
    ele = int(input(f"Enter threshold {i+1}: "))
    lst.append(ele)

for t in lst:
    result = grayscale.copy()   
    ht, wt = result.shape
    for i in range(ht):
        for j in range(wt):
            if result[i][j] < t:
                result[i][j] = 0
            else:
                result[i][j] = 255
    print(f"Threshold = {t}")
    plt.imshow(result, cmap="gray")
    plt.show()
