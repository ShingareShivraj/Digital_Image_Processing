import cv2
src = cv2.imread('car.jpg')
img=cv2.resize(src, (300, 300))
print (src.shape)
print(img.shape)
cv2.imshow('Original',src)
cv2.imshow('Resize',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
