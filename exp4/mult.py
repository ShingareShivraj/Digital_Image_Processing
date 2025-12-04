import cv2
image1 = cv2.imread('car.jpg')
print(image1.shape)
image4=cv2.resize(image1, (485,718))
cv2.imshow("first img",image4)
cv2.waitKey(0)

image2 = cv2.imread('nature.png')
print(image2.shape)
cv2.imshow("second img",image2)
cv2.waitKey(0)

addition = cv2.multiply(image2, image4)
cv2.imshow("Added img",addition)
cv2.waitKey(0)
