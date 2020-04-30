import argparse
import cv2
import numpy as np

# Thresholding converts the grayscale image into binary format, either black or white no other shades
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray ", gray)

# Applying Gaussian Blurring helps remove some of the high frequencey edges in the image that we're not interested in
# std dev is 5
blurred = cv2.GaussianBlur(gray, (5,5), 0)

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary", threshInv)

cv2.imshow("Images", cv2.bitwise_and(gray, gray, mask=threshInv))
cv2.waitKey(0)


