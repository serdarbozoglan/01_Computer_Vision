import numpy as np 
import cv2
import imutils
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])

# Original image
cv2.imshow("Original image", image)
cv2.waitKey(0)

# Resized width
resized = imutils.resize(image, width=100)
cv2.imshow("Resized width", resized)
cv2.waitKey(0)

# Resized height
resized = imutils.resize(image, height=60)
cv2.imshow("Resized Height", resized)
cv2.waitKey(0)


