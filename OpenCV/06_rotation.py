import numpy as np 
import cv2
import imutils
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])

# rotate 180 degree
rotated = imutils.rotate(image, 180)
cv2.imshow("180 rotated", rotated)
cv2.waitKey(0)

# rotate 60 degree
rotated = imutils.rotate(image, 60)
cv2.imshow("180 rotated", rotated)
cv2.waitKey(0)
