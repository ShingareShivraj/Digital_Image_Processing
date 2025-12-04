import cv2
src=cv2.imread('car.jpg')
percent=50
print(src.shape)
width=src.shape[1]
w = int(width * percent / 100)
height=src.shape[0]
h = int(height * percent / 100)
resize=cv2.resize(src,(h,w))
print(resize.shape)
cv2.imshow("Resize", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()