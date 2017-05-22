import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def get_image():
	retval, im = cap.read()
	return im
	

while(True):
	# capture frame by frame
	
	ret, frame = cap.read()
	
	# our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Display the resulting frame
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
	
	for i in xrange(1):
		temp = get_image()
	print("Taking image...")
	
	camera_capture = get_image()
	file = "/home/odroid/Desktop/python_scripts/test/test_images/test_image1.png"
	cv2.imwrite(file, camera_capture)
	
		
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
	
