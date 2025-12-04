import cv2
import numpy as np

image1 = cv2.imread('car.jpg')
image=cv2.resize(image1,(400,400))
if image is None:
    print("Image not found!")
    exit()

image_float = np.float32(image)
c = 255 / np.log(1 + np.max(image_float))
log_image = c * (np.log(image_float + 1))
log_image = np.array(log_image, dtype=np.uint8)

cv2.imshow('Log Transform', log_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
