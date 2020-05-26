import numpy as np 
import cv2
import math
from scipy import ndimage
import pytesseract

IMAGE_PATH = "Data/image_to_rotate.jpeg"

img = cv2.imread(IMAGE_PATH)
# cv2.imshow("image", img)
# cv2.waitKey(0)


## ORIENTATION CORRECTION/ADJUSTMENT
def orientation_correction(img, save_image=False):

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Canny Alg for edge detection
    imgEdges = cv2.Canny(imgGray, 100, 100, apertureSize=3)

    # Using Houglines to detect lines
    imgLines = cv2.HoughLinesP(imgEdges, 1, math.pi/180.0, 100, minLineLength=100, maxLineGap=5)

    # Finding angles of lines in polar cordinates
    angles = []

    for x1, y1, x2, y2 in imgLines[0]:
        angle = math.degrees(math.atan2(y2-y1, x2-x1))
        angles.append(angle)

    # Getting the median angle
    median_angle = np.median(angles)

    imgRotated = ndimage.rotate(img, median_angle)

    if save_image:
        cv2.imwrite('Data/orientation_corrected.jpg', imgRotated)
    return imgRotated

imgRotated = orientation_correction(img,save_image=True)

## REGION OF INTEREST (ROI) SELECTION
# REGION OF INTEREST (ROI) SELECTION

# initializing the list for storing the coordinates 
coordinates = [] 
  
# Defining the event listener (callback function)
def shape_selection(event, x, y, flags, param): 
    # making coordinates global
    global coordinates 
  
    # Storing the (x1,y1) coordinates when left mouse button is pressed  
    if event == cv2.EVENT_LBUTTONDOWN: 
        coordinates = [(x, y)] 
  
    # Storing the (x2,y2) coordinates when the left mouse button is released and make a rectangle on the selected region
    elif event == cv2.EVENT_LBUTTONUP: 
        coordinates.append((x, y)) 
  
        # Drawing a rectangle around the region of interest (roi)
        cv2.rectangle(image, coordinates[0], coordinates[1], (0,0,255), 2) 
        cv2.imshow("image", image) 
  
  
# load the image, clone it, and setup the mouse callback function 
image = imgRotated


image_copy = image.copy()
cv2.namedWindow("image") 
cv2.setMouseCallback("image", shape_selection) 
  
  
# keep looping until the 'q' key is pressed 
while True: 
    # display the image and wait for a keypress 
    cv2.imshow("image", image) 
    key = cv2.waitKey(1) & 0xFF
  
    if key==13: # If 'enter' is pressed, apply OCR
        break
    
    if key == ord("c"): # Clear the selection when 'c' is pressed 
        image = image_copy.copy() 
  
if len(coordinates) == 2: 
    image_roi = image_copy[coordinates[0][1]:coordinates[1][1], 
                           coordinates[0][0]:coordinates[1][0]] 
    cv2.imshow("Selected Region of Interest - Press any key to proceed", image_roi) 
    cv2.waitKey(0) 
  
# closing all open windows 
cv2.destroyAllWindows()  

# keep looping if 'q' key is pressed
while True:

    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == 13: # if Enter is pressed apply OCR
        break

    if key == ord('c'): # Clear the selection when 'c' is pressed
        image = image_copy.copy()

if len(coordinates) == 2:
    image_roi = image_copy[coordinates[0][1]:coordinates[1][1],
                            coordinates[0][0]:coordinates[1][0]]

    cv2.imshow('Selected Region of Intrest - Press any key to proceed', image_roi)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# OPTICAL CHARACTER RECOGNITION (OCR) ON ROI
text = pytesseract.image_to_string(image_roi)
print('The text in the semlected region is as follows:')
print(text)
