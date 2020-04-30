import argparse
import cv2

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg.parse_args())

#cv2.imread loads the image and converst into numpy
image = cv2.imread(args["image"])

print("width : {} pixels".format(image.shape[1]))
print("height : {} pixels".format(image.shape[0]))
print("channels : {} pixels".format(image.shape[2]))

# load image into cv2 window
# wait for key press
# write the image to another format
cv2.imshow("Image Title", image)
cv2.waitKey(0)
cv2.imwrite("newcat.jpg", image)