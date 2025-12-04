import cv2
image=cv2.imread('nature.png')
images = cv2.transpose(image)
cv2.imshow('Sample Image', images)
cv2.waitKey(0)
cv2.destroyAllWindows()
