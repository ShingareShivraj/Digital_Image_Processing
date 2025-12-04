import numpy as np
import cv2

red_img = np.zeros((300, 300, 3), dtype=np.uint8)
red_img[:] = [0, 0, 255]  

cv2.imshow("Red Image", red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
