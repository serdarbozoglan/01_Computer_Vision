import argparse
import cv2
import numpy as np

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# generating one array and multiplying with 100
# adding that array to the actual image
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added image", added)
# cv2.waitKey(0)

# generating one array and multiplying with 50
# substrcuting that array to the actual image
M = np.ones(image.shape, dtype="uint8") * 50
substracted = cv2.subtract(image, M)
cv2.imshow("Substructed image", substracted)
cv2.waitKey(0)