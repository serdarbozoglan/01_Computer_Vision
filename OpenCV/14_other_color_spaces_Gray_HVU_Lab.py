import argparse
import cv2
import numpy as np

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])
cv2.imshow("BGR Color Space", image)


# BGR to GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY Color Space", gray)


# BGR to HSV (Hue Saturation Value)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Color Space", hsv)


# BGR to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("Lab Color Space", lab)
cv2.waitKey(0)