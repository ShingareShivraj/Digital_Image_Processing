import cv2


img=cv2.imread("car.jpg")
layer=img.copy()

for i in range(4):
    
    layer=cv2.pyrDown(layer)
    cv2.imshow("str(i)", layer)
    cv2.waitKey(0)


cv2.destroyAllWindows()