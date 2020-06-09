import cv2
import numpy as np 

img = cv2.imread('Data/image1.jpg')
# Shape returns "H x W x Channel"
print(img.shape)

# RESIZING
# Resize yaparken tupple icine ONCE WIDTH SONRA HEIGHT yaziyoruz
# Shape'in tersi
imgResized = cv2.resize(img, (200,400))
print(imgResized.shape)

## CROPPING
# Height comes first in matrix
imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Resized", imgResized)
cv2.imshow('Cropped', imgCropped)
cv2.waitKey(0)