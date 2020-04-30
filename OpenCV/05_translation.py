import numpy as np
import cv2
import imutils
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])

# shift image down
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down image : ", shifted)
cv2.waitKey(0)

# shift image up
shifted = imutils.translate(image, 0, -100)
cv2.imshow("Shifted Up image : ", shifted)
cv2.waitKey(0)

# shift image right
shifted = imutils.translate(image, 100, 0)
cv2.imshow("Shifted Right image : ", shifted)
cv2.waitKey(0)

# shift image left
shifted = imutils.translate(image, -100, 0)
cv2.imshow("Shifted Left image : ", shifted)
cv2.waitKey(0)