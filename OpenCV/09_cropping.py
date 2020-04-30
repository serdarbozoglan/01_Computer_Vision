import numpy as np 
import cv2
import imutils
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])
cv2.imshow("Original image", image)
print("width : {} pixels".format(image.shape[1]))
print("height : {} pixels".format(image.shape[0]))
print("channels : {} pixels".format(image.shape[2]))
cv2.waitKey(0)

# Crop the image
# start y:20 end y:450, start x:350 end x:900
cropped = image[100:1000, 250:1500]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
