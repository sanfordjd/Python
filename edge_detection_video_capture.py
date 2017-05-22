import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(0)

while(True):
	# capture frame by frame
	
	ret, frame = cap.read()
	
	#flip image
	frame = cv2.flip(frame, 1)
		
	# make grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# run Canny Edge Detection
	edges = cv2.Canny(frame, 100, 200)
	
	# Display the resulting frame
	cv2.imshow('image', edges)
	
	k = cv2.waitKey(30) & 0xff
	if k == ord('q'):
		break
	elif k == 27:
		break
	
	
			
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
	
