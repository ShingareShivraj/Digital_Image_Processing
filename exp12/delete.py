import cv2
from skimage import io
from skimage.filters import threshold_sauvola
from skimage.filters import threshold_niblack

image=cv2.imread('car.jpg', 0)
image=cv2.resize(image, (300,300))
cv2.imshow('resize_image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#simple threshold
_, image1=cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("simple threshold",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#otsu threshold
_,image2=cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("otsu image", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#sauvola threshold

binary=threshold_sauvola(image, window_size=25)
image3=image>binary
cv2.imshow("sauvola image", (image3*255).astype('uint8'))
cv2.waitKey(0)
cv2.destroyAllWindows()

#niblack threshold
threshold=threshold_niblack(image, window_size=25)
image4=image>threshold
cv2.imshow("niblack image",(image4*255).astype('uint8'))
cv2.waitKey(0)
cv2.destroyAllWindows()