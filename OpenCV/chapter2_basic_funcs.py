import cv2
import numpy as np

img = cv2.imread('Data/image1.jpg')
kernel = np.ones((5,5), np.uint8) 
# to Gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur should be odd numbers (3,3) or (5,5) so on
# The Higher numbers in kernel size the more blurred
imgBlur = cv2.GaussianBlur(img, (7,7), 0)

# Finding edges in the image
# The higher numbers less edges
imgCanny1 = cv2.Canny(img, 100, 100)
imgCanny2 = cv2.Canny(img, 200, 200)

# Bazen edge detect ederken cizgiler birlesmez
# Bunu cizgilerin kalinligini artirarak cozebiliriz
# the more iteration the ticker lines
imgDialation = cv2.dilate(imgCanny1, kernel, iterations=1)

# Errosion, lessens the tickess of lines
# Opposite to Dialation
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny1", imgCanny1)
cv2.imshow("Canny2", imgCanny2)
cv2.imshow('Dialation', imgDialation)
cv2.imshow("Erroded", imgEroded)
cv2.waitKey(0)