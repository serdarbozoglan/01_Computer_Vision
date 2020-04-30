import argparse
import cv2
import numpy as np

# Gradient is directional chnage in the intensity or color of the image 
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])


# GRAY needs tobe used
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# LAPLASIAN
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplasian", lap)
cv2.waitKey(0)

# SOBEL EDGE DETCTION
# X eksenindeki ve Y eksenindeki edge'leri tespit ederiz
sobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow('Sobel X', sobelX)
cv2.imshow('Sobel Y', sobelY)
cv2.imshow('Sobel Combined', sobelCombined)
cv2.waitKey(0)