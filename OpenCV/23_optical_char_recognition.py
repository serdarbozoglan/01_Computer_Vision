from PIL import Image
import pytesseract
import argparse
import cv2
import os

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
arg.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")

args = vars(arg.parse_args())

# prepocess: The preprocessing method, This switch is optional and can accept 2 values (threshold or blur)

image =  cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if args['preprocess'] =='thresh':
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# blur is used for removing the noise from image
elif args['preprocess'] == 'blur':
    gray = cv2.medianBlur(gray,3)

# write the graysclae image to disk as an temp file so we can apply OCR to it
# getpid --> returns process id 
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as PIL/Pillow image apply OCR and then delete teh temp file
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

cv2.imshow("Image", image)
cv2.imhshow("Output", gray)
cv2.waitKey(0)