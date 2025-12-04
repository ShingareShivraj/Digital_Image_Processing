import cv2
img1=cv2.imread("nature.png")
x=cv2.resize(img1,(300,300))

img2=cv2.imread("car.jpg")
img3=cv2.resize(img2,(300,300))
i=cv2.multiply(img3, x)
cv2.imshow("multiply",i)
cv2.waitKey(0)