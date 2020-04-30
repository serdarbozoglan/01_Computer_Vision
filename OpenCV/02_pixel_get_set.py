import argparse
import cv2

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])

b, g, r = image[0,0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# chnage the color of the pixel
image[0,0] = (0, 0, 255)
b, g, r = image[0, 0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Grab the portion of an image
corner = image[0:100, 0:100]
cv2.imshow("Sliced Corner", corner)
cv2.waitKey(0)

# Change color of the selected area
# color order is Blue, Green, Red not RGB
image[0:100,0:100] = (0, 255, 0)
cv2.imshow("Edited Image: ", image)
cv2.waitKey(0)

