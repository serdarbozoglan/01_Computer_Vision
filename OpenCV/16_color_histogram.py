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

channels = cv2.split(image)
colors = ('b','g', 'r')
plt.figure()
plt.title('Flattened Color Histogram')
plt.xlabel("Bins")
plt.ylabel('# of Pixels')

for (channel, color) in zip(channels, colors):
    # params             (images, channels, mask, histSize, ranges)
    hist = cv2.calcHist([channel], [0],      None,   [256],   [0,256])
    plt.plot(hist, color=color)
    plt.xlim([0,256])

plt.show()
cv2.waitKey(0)