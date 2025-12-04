import cv2
import numpy as np
img=cv2.imread("car.jpg")
car=cv2.resize(img, (400,300))
cv2.imshow("car",car)
cv2.waitKey(0)

#negative
max=np.max(car)
negative=max-car
cv2.imshow("car",negative)
cv2.waitKey(0)
cv2.destroyAllWindows()