import numpy as np 
import cv2

canvas = np.zeros((300,300, 3), dtype='uint8')

green = (0, 255, 0)

# (100,100) --> center of circle and radious is 10
cv2.circle(canvas, (100,100), 10, green)
cv2.imshow("Single circle", canvas)
cv2.waitKey(0)

# draw concetric white cirlcles
white = (255,255,255)

centerX = canvas.shape[1]//2 
centerY = canvas.shape[0]//2 

# clearing the canvas
canvas = np.zeros((300,300, 3), dtype='uint8')

# generating circles with for loop
for radious in range(0, 175, 25):
	cv2.circle(canvas, (centerX, centerY), radious, white, 2)
cv2.imshow('Concentric Circles', canvas)
cv2.waitKey(0)

canvas = np.zeros((300,300, 3), dtype='uint8')

# draw 25 circles
for i in range(0,25):
	radius = np.random.randint(5, high=200) 
	color = np.random.randint(0, 256, size=(3,)).tolist()
	# Center point includes 2 points for x and y
	center_pt = np.random.randint(0, high=300, size=(2,)) # for x and y
	cv2.circle(canvas, tuple(center_pt), radius, color, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)