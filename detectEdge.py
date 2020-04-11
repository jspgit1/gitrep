import cv2
import numpy as np

img = cv2.imread('car.png',1)
print(type(img))
cv2.imshow('Car Window',img)
cv2.waitKey(0)
cv2.destroyWindow('Car Window')

# Use cv2.Canny(image, minVal, maxVal) to detect edge of image
detectedge1 = cv2.Canny(img, 10, 20)
detectedge2 = cv2.Canny(img, 30, 60)
detectedge3 = cv2.Canny(img, 50, 100)
detectedge4 = cv2.Canny(img, 100, 200)
detectedge5 = cv2.Canny(img, 200, 500)

cv2.imshow('Original Image', img)
cv2.imshow('Detect edge image-(10,20)', detectedge1)
cv2.imshow('Detect edge image-(30,60)', detectedge2)
cv2.imshow('Detect edge image-(50,100)', detectedge3)
cv2.imshow('Detect edge image-(100,200)', detectedge4)
cv2.imshow('Detect edge image-(200,500)', detectedge5)

while True:
	if cv2.waitKey(10) & 0xFF == ord('q'):
		#cv2.destroyAllWindows()
		break
