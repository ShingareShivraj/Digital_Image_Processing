import cv2
image=cv2.imread('nature.png')
cv2.imshow('Sample Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()