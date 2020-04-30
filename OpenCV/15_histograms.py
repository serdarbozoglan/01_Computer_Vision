import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])

# Histogram shows the distribution of the pixel intensities (colorful or gray-scale) 
# cv2.calcHist ---> params (images, channels, mask, histSize, ranges)
# images should be in a list even a single image it shoud be [image]
# for channels, grey images should be [0] for RB [0,1,2]
# mask --> optinal
# histSize is the y axis of the graph (number of pixels)
# ranges --> [0,256] for each channel

# BGR to GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY Color Space", gray)



#params            (images, channels, mask, histSize, ranges)
hist = cv2.calcHist([gray], [0],     None, [256], [0,256])

plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
