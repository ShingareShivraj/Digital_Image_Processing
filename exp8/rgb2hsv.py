import cv2
import numpy as np
import math

img = cv2.imread('car.jpg')
bgr = np.float32(img) / 255
b, g, r = bgr[:,:,0], bgr[:,:,1], bgr[:,:,2]

# Intensity
I = (r + g + b) / 3

# Saturation
minimum = np.minimum(np.minimum(r, g), b)
S = 1 - (3 * minimum / (r + g + b + 0.001))

# Hue
num = 0.5 * ((r - g) + (r - b))
denom = np.sqrt((r - g)**2 + (r - b)*(g - b))
theta = np.clip(num / (denom + 1e-8), -1, 1)  # avoid NaN

H = np.arccos(theta)

# Adjust hue based on B,G relationship
H[b > g] = (2 * math.pi) - H[b > g]

# Normalize hue to [0,1]
H = H / (2 * math.pi)

# Merge all channels
hsi = cv2.merge([H, S, I])

# Display
img_resized = cv2.resize(img, (600, 600))
hsi_resized = cv2.resize(hsi, (600, 600))
hsi_display = np.uint8(hsi_resized * 255)
x = np.hstack((img_resized, hsi_display))

cv2.imshow('Original (left) and HSI (right)', x)
cv2.waitKey(0)
cv2.destroyAllWindows()
