import threading
# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np

#Import the thread class
def draw_rectangle(img, pt1, pt2, color, thickness, d):
    x1,y1 = pt1
    x2,y2 = pt2
    
    # Top left
    #cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    #cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    #cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)
    cv2.line(img, (x1 , y1), (x1 + d, y1), color, thickness)
    cv2.line(img, (x1, y1 ), (x1, y1 + d), color, thickness)
    
    # Top right
    #cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    #cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    #cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)
    cv2.line(img, (x2 , y1), (x2  - d, y1), color, thickness)
    cv2.line(img, (x2, y1 ), (x2, y1 + d), color, thickness)
    
    # Bottom left
    #cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    #cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    #cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)
    cv2.line(img, (x1 , y2), (x1 + d, y2), color, thickness)
    cv2.line(img, (x1, y2 ), (x1, y2 - d), color, thickness)
    
    # Bottom right
    #cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    #cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    #cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)
    cv2.line(img, (x2 , y2), (x2 - d, y2), color, thickness)
    cv2.line(img, (x2, y2 ), (x2, y2 - d), color, thickness)

cascadePath = "haarcascade_frontalface_default.xml"
#cascadePath = "eye.xml"
# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Ip of the IP webcam server (on phone). The phone and your computer must be in the same LAN (connected to the same WiFi)
#url = 'rtsp://admin:admin123@192.168.1.62/1'
url = 0
video_capture = cv2.VideoCapture(0)

while True:
    # Read the video frame from the url

    ret, frame = video_capture.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(frame, 1.3,5)

    for (x, y, w, h) in faces:
       #img  initial    final    (r,  g , b), thickness
       #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
       draw_rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),4, 30)
       # Display the video frame with the bounded rectangle
    cv2.imshow('im',frame)

        # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
