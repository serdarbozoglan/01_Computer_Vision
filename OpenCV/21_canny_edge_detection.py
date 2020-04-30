import argparse
import cv2
import numpy as np

# IT IS BETTER EDGE DETECTION

# It is multi-step process
# It involves blurring to remove the noise
# Computing Sobel Gradient images in the X and Y direction
# we provide 2 thresholds, ay gradient value greater than threshold2 is regarded as "edge"
# any avlue below than threshold1 is NOT edge
# values between threshold1 and threshold2 either classified as edge or not

# Gradient is directional chnage in the intensity or color of the image 
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])


# GRAY needs to be used
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("Blurred", blurred)

canny = cv2.Canny(blurred, 30, 150)
cv2.imshow('Canny', canny)
cv2.waitKey(0)