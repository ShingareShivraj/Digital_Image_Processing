
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('nature.png')            # Read color image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

blurred = cv2.GaussianBlur(gray, (3,3), 0)
edges = cv2.Canny(blurred, 50, 150, apertureSize=3)

lines = cv2.HoughLinesP(edges, 
                        rho=1,                   # Distance resolution (1 pixel)
                        theta=np.pi/180,         # Angle resolution (1 degree)
                        threshold=50,            # Minimum votes to detect a line
                        minLineLength=50,        # Minimum length of a line segment
                        maxLineGap=10)           # Max g
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.imshow(edges, cmap='gray')
plt.title('Detected Edges (Canny)')

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Detected Lines using Hough Transform')

plt.show()
