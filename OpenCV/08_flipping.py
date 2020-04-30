import numpy as np 
import cv2
import imutils
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])

# Vertical Flip
flipped =cv2.flip(image, 0)
cv2.imshow("Vertical Flip", flipped)
cv2.waitKey(0)

# Horizantal Flip
flipped =cv2.flip(image, 1)
cv2.imshow("Horizantal Flip", flipped)
cv2.waitKey(0)

# Both Flip
flipped =cv2.flip(image, -1)
cv2.imshow("Both Flip", flipped)
cv2.waitKey(0)