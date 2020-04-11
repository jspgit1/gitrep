import cv2
import numpy as np

img = cv2.imread('car.png',1)
print(type(img))
cv2.imshow('Car Window',img)
cv2.waitKey(0)
cv2.destroyWindow('Car Window')

# Use GaussianBlur() to blurry the image
bluredimg1 = cv2.GaussianBlur(img, (7,7), 0)
bluredimg2 = cv2.GaussianBlur(img, (91,91), 0)

cv2.imshow('Original Image', img)
cv2.imshow('Blured image-(7,7)', bluredimg1)
cv2.imshow('Blured image-(91,91)', bluredimg2)

cv2.waitKey(0)


cv2.destroyAllWindows()
