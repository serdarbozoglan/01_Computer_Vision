import cv2

# Importing an image
# img = cv2.imread("Data/image1.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# Importing a video
cap = cv2.VideoCapture('Data/video1.mp4')

# Capturing from webcam
cap = cv2.VideoCapture(0) # 0 means webcam
cap.set(3, 640) # height id=3, height=680
cap.set(4, 480) # width id=4, width=480

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0XFF ==ord('q'):
        break