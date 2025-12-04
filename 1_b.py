import cv2
image=cv2.imread('nature.png')
images = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) 
cv2.imshow('Sample Image', images)
cv2.waitKey(0)
cv2.destroyAllWindows()