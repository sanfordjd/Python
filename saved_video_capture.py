#!/usr/bin/env python

import numpy as np
import cv2

#img0 = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/test_image1.png')

cap = cv2.VideoCapture('/home/odroid/Desktop/python_scripts/test/test_images/Default_Project1.mp4')

#cv2.imshow('image0', img0)

while(cap.isOpened()):
	ret, frame = cap.read()
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	cv2.imshow('frame', gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.waitKey(0)
cv2.destroyAllWindows()
