import numpy as np 
import cv2

# create an image 250x250 white rectangle inside 300x300
# create a 150 radius white circle inside 300x300
rectangle = np.zeros((300, 300), dtype='uint8')
cv2.rectangle(rectangle, (25,25), (275,275), 255, -1) # 255 color code is white, -1 means fill it
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype='uint8') # 0 larla doldurmak esasisnda siyah pixels
cv2.circle(circle, (150,150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

bitwiseAnd  = cv2.bitwise_and(rectangle, circle)
cv2.imshow("Bitwise And", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr  = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Bitwise Or", bitwiseOr)
cv2.waitKey(0)

bitwiseXor  = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("Bitwise Xor", bitwiseXor)
cv2.waitKey(0)

bitwiseNot  = cv2.bitwise_not(rectangle, circle)
cv2.imshow("Bitwise Not", bitwiseNot)
cv2.waitKey(0)

