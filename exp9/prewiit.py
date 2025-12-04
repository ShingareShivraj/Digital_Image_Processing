import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
img = cv2.imread('nature.png')   
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
gray = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY) 
img = cv2.GaussianBlur(gray,(3,3),0) 
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]]) 
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]]) 
img_prewittx = cv2.filter2D(img, -1, kernelx) 
img_prewitty = cv2.filter2D(img, -1, kernely) 
cv2.imshow("Prewitt", img_prewittx + img_prewitty) 
cv2.waitKey(0)