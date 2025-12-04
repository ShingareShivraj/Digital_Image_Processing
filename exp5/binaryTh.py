import cv2 
import numpy as np 
image = cv2.imread('car.jpg') 
image=cv2.resize(image,(400,400))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,thresh1 =cv2.threshold(image,70,255,cv2.THRESH_BINARY_INV) 
cv2.imshow("Threshold Binary inverse", thresh1) 
cv2.waitKey(0) 