import cv2
import numpy as np

img = cv2.imread('car.png',1)
print(type(img))
cv2.imshow('Car Window',img)
cv2.waitKey(0)
#cv2.destroyWindow('Car Window')

# new_img = a * original_img + b. a is 0 to x. b is -127 to 127
# a is for contrast. b is for brightness
contrast_img1 = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
contrast_img2 = cv2.addWeighted(img, 0.5, np.zeros(img.shape, img.dtype), 0, 0)
cv2.imshow('Original Image', img)
cv2.imshow('Contrast Image-2.5', contrast_img1)
cv2.imshow('Contrast Image-0.5', contrast_img2) 
while True:
	if cv2.waitKey(10) & 0xFF == ord('q'):
		#cv2.destroyAllWindows()
		break
