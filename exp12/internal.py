import cv2
from skimage import io
from skimage.filters import threshold_sauvola
from skimage.filters import threshold_niblack

img = cv2.imread('natre.png' , cv2.IMREAD_GRAYSCALE)  
_, th_simple = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Simple Threshold", th_simple)
cv2.waitKey(0)
cv2.destroyAllWindows()


_, th_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("Otsu Threshold", th_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()


window_size = 25
thresh_sauvola = threshold_sauvola(img, window_size=window_size)
binary_sauvola = img > thresh_sauvola

cv2.imshow("Sauvola Threshold", (binary_sauvola * 255).astype('uint8'))
cv2.waitKey(0)
cv2.destroyAllWindows()



window_size = 25
thresh_niblack = threshold_niblack(img, window_size=window_size, k=0.2)
binary_niblack = img > thresh_niblack

cv2.imshow("Niblack Threshold", (binary_niblack * 255).astype('uint8'))
cv2.waitKey(0)
cv2.destroyAllWindows()
