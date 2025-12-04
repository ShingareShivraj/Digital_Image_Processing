import cv2 
img=cv2.imread("nature.png") 
t_upper=50 
t_lower=150 
edge=cv2.Canny(img,t_lower,t_upper) 
cv2.imshow('original',img) 
cv2.waitKey(0) 
cv2.imshow('Canny',edge) 
cv2.waitKey(0)