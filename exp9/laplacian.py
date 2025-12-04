import cv2 
img=cv2.imread("nature.png") 
laplacian=cv2.Laplacian(img,cv2.CV_64F) 
cv2.imshow('original',img) 
cv2.waitKey(0) 
cv2.imshow('Laplacian',laplacian) 
cv2.waitKey(0) 