import numpy as np 
import cv2

# define a canvas of size 300x300 px with 3 channnels (R,G,B) and data type unit8
canvas = np.zeros((300, 300, 3), dtype="uint8")

# define color
green = (0, 255, 0)
# draw the line from coordinate of (0,0) to (300, 300), tickness is optional
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow('The canvas', canvas)
cv2.waitKey(0) 

# draw line with width
red = (0, 0, 255)
# draw the line from coordinate of (0,0) to (300, 300)
# red den sonraki parametre 3 --> cizgi kalinligi
cv2.line(canvas, (0,0), (300,300), red, 3)
cv2.imshow('The canvas', canvas)
cv2.waitKey(0) 

# draw rectengales
cv2.rectangle(canvas, (200,20), (240,120), red, 2)
cv2.imshow('The canvas', canvas)
cv2.waitKey(0) 

# to fill the rectengle use -1
cv2.rectangle(canvas, (200,20), (240,120), green, -1)
cv2.imshow('The canvas', canvas)
cv2.waitKey(0) 
