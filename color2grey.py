import cv2
import numpy as np

img = cv2.imread('car.png',1)
print(type(img))
cv2.imshow('Car Window',img)
cv2.waitKey(0)
cv2.destroyWindow('Car Window')

# Use cv2.cvtColor to convert color image to greyscale image
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)


cv2.imshow('Original Image', img)
cv2.imshow('Color to greyscale', img1)
cv2.imshow('Color to HSV', img2)




cv2.waitKey(0)


cv2.destroyAllWindows()
