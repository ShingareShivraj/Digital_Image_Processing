import cv2
import numpy as np

image1 = cv2.imread('car.jpg')
image=cv2.resize(image1,(400,400))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

normalized = image / 255.0
gamma = 0.5   
gamma_corrected = np.power(normalized, gamma)
gamma_corrected = np.uint8(gamma_corrected * 255)

cv2.imshow("Original", image)
cv2.imshow("Gamma Corrected", gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()
