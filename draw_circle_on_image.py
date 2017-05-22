Great!import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(0)

while(True):
	# capture frame by frame
	
	ret, frame = cap.read()
	
	
	frame = cv2.flip(frame, 1)
		
	# our operations on the frame come here
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	cv2.circle(frame, (200,200), 40, (0,0,255), 10)
	
	# Display the resulting frame
	cv2.imshow('image',frame)
	
	#cv2.circle(gray
	
	if cv2.waitKey(1) == 27:
		break
	
	
	
	
		
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
	
