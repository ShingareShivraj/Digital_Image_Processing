import cv2
import numpy as np
img=cv2.imread("car.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original image", img)
cv2.waitKey(0)  
cv2.destroyAllWindows()

def quantize(img, levels):
    max_val=256
    step=max_val//levels
    x= (img // step)* step
    return x

q4=quantize(img, 4)
q16=quantize(img, 16)
q64=quantize(img, 64)

cv2.imshow("original image", img)
cv2.imshow("4 level", q4)
cv2.imshow("16 level", q16)
cv2.imshow("64 level", q64)
cv2.waitKey(0)
cv2.destroyAllWindows()
