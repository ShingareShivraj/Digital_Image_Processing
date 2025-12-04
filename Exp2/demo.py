import cv2
image=cv2.imread('car.jpg')
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('image', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
