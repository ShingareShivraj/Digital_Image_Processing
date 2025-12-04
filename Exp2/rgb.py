import cv2
x=cv2.imread('car.jpg')
cv2.imshow('real image',x)
cv2.waitKey(0)
cv2.destroyAllWindows()
image=cv2.imread('car.jpg')
image[:,:,0]=0
image[:,:,1]=0
red=cv2.imshow('red image', image)
cv2.waitKey(0)


#blue image
image[:,:,1]=0
image[:,:,2]=0
blue=cv2.imshow('blue image', image)
cv2.waitKey(0)


#green image
image[:,:,0]=0
image[:,:,2]=0
green=cv2.imshow('green image', image)  
cv2.waitKey(0)
cv2.destroyAllWindows()

max1=image.max()
negimg=max1-image
cv2.imshow('Negative Image', negimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Sample Image', gray_image)
cv2.waitKey(0)

hsv_image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

ycbcr_image=cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
cv2.imshow('YCrCb Image', ycbcr_image)  
cv2.waitKey(0)
cv2.destroyAllWindows()

rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

flip_vertical = cv2.flip(image, 0)
cv2.imshow('Flipped Image', flip_vertical)  
cv2.waitKey(0)
cv2.destroyAllWindows()

flip_horizontal = cv2.flip(image, 1)
cv2.imshow('Flipped Image', flip_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()

flip_both = cv2.flip(image, -1)
cv2.imshow('Flipped Image', flip_both)      
cv2.waitKey(0)
cv2.destroyAllWindows()

transposeimg= cv2.transpose(image)
cv2.imshow('Transposed Image', transposeimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

