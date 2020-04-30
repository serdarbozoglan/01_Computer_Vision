import argparse
import cv2
import numpy as np

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])


# as the kernels size increases blurring also increses
# k is an alwyas odd number and size must be "k x k"
blurred = np.hstack([
    cv2.blur(image, (3,3)),
    cv2.blur(image, (5,5)),
    cv2.blur(image, (7,7))
])

cv2.imshow("Origainal vs Average Blured", np.hstack([image, blurred]))
cv2.waitKey(0)


# GAUSSIAN BLUR
# 0 is the sd dev 
gaussian_blurred = np.hstack([
    cv2.GaussianBlur(image, (3,3), 0),
    cv2.GaussianBlur(image, (5,5), 0),
    cv2.GaussianBlur(image, (7,7), 0)
])

cv2.imshow("Origainal vs Gaussian Blured", np.hstack([image, gaussian_blurred]))
cv2.waitKey(0)

# MEDIAN BLUR
median_blurred = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)
])

cv2.imshow("Origainal vs Median Blured", np.hstack([image, median_blurred]))
cv2.waitKey(0)

# BILATERAL
bilateral_blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)
])

cv2.imshow("Origainal vs Bilateral Blured", np.hstack([image, bilateral_blurred]))
cv2.waitKey(0)