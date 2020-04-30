import argparse
import cv2
import numpy as np

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])


# MASKING --> USING RECTANGLE
# construct an np array flled with zeros with the same width and height of an image
# compute the center point of the image and draw a white rectangle 
mask = np.zeros(image.shape[:2], dtype='uint8') # cnavas
(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
# 150x150 lik bir rectange tanimliyoruz, white ile fill ediyourz
cv2.rectangle(mask, (cX-75, cY-75), (cX+75, cY+75), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Maked Applied to Image", masked)
cv2.waitKey(0)

# MASKING --> USING CIRCLE
# construct an np array flled with zeros with the same width and height of an image
# compute the center point of the image and draw a white rectangle 
mask = np.zeros(image.shape[:2], dtype='uint8') # cnavas
(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
# 150x150 lik bir rectange tanimliyoruz, white ile fill ediyourz
radius = 90
# asadikdai center'dan off yapan +90 -5 gibi sayilari deneme yanilma ile ekledim
cv2.circle(mask, (cX+90, cY-5),radius, 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Maked Applied to Image", masked)
cv2.waitKey(0)