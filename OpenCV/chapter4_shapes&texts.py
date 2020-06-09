import cv2
import numpy as np 

# creating 512x512 black canvas
img = np.zeros((512,512))
print(img.shape)

# 3 color canvas
img2 = np.zeros((512, 512, 3), np.uint8)
# Blue Canvas
img2[:] = 255, 0, 0
# Green Canvas
img3 = np.zeros((512, 512, 3), np.uint8)
img3[:] = 0, 255, 0

# DRAWING A LINE
# from (0,0) to (300, 300), (color green (0, 255, 0), tickness=3)
img4 = cv2.line(img2, (0,0), (300, 300), (0, 255, 0), 3)
img5 = cv2.line(img2, (0,0), (img2.shape[1], img.shape[0]), (0 ,0, 100), 3)

# DRAWING A RECTANGLE
img6 = cv2.rectangle(img2, (0,0), (250, 350), (0, 0, 255), cv2.FILLED)

cv2.imshow("Black", img)
cv2.imshow("Blue", img2)
cv2.imshow('Green', img3)
cv2.imshow('Green Lined', img4)
cv2.imshow('Color Lined', img5)
cv2.imshow('Rectangle', img6)
cv2.waitKey(0)