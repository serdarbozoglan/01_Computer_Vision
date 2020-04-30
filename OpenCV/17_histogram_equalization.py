import argparse
import cv2
import numpy as np

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])

# histogram equalization smooths the image and improves the contrast of the image
# histogram equalization can be applied to ONLY GRAYSCALE
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Gray Scaled Image", gray)
cv2.waitKey(0)

eq = cv2.equalizeHist(gray)
cv2.imshow("Histogram Equalization Image", np.hstack([gray, eq]))
cv2.waitKey(0)