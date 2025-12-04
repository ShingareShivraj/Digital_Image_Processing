import cv2
import matplotlib.pyplot as plt

img = cv2.imread('nature.png', 0)

blur = cv2.GaussianBlur(img, (5, 5), 0)

ret1, th1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

ret2, th2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

titles = ['Original Image', 'Simple Thresholding', 'Otsu Thresholding']
images = [img, th1, th2]

plt.figure(figsize=(10,6))
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
