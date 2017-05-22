import cv2
import numpy as np

def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im

file = "/home/odroid/Desktop/test_image.png"

#Update OpenCV object with latest from camera
#opencv.loadImage(video);

cap = cv2.VideoCapture('/home/odroid/Desktop/python_scripts/test/test_images/Edited_Foam_Dispense_Short.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
		s, im = cap.read()
		cv2.imwrite(file, im)
		break

cap.release()
cv2.destroyAllWindows()
	
