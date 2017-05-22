#Joe Sanford
#APR2017
#***********************************************************************
# This code finds a possible foam up condition given a single frame of a
# recorded video from a Speedy Packer 
# This video is taken from a simple webcam through the opaque bag and
# as mounted inside the Speedy Packer pointed at the dispensing nozzle
#***********************************************************************

#***********************************************************************
#******************************Import***********************************
#***********************************************************************

import cv2
import numpy as np
import imutils 

np.set_printoptions(threshold=np.inf) #to print entire array, no truncation

#***********************************************************************
#******************************Variables********************************
#***********************************************************************

LOWER_BOUND = 55   #cv2.threshold()
UPPER_BOUND = 255  #cv2.threshold()

CANNY_LOWER_BOUND = 10  #cv2.Canny()
CANNY_UPPER_BOUND = 250 #cv2.Canny()

MIN_LINE_LENGTH = 2  #HoughLinesP()
MAX_LINE_GAP = 100     #HoughLinesP() 
HOUGH_THETA = np.pi/180 #HoughLinesP() angle resolution of the accumulator, radians
HOUGH_THRESHOLD = 25 #HoughLinesP() 
HOUGH_RHO = 1         #HoughLinesP() rho, Distance resolution of the accumulator, pixels

low_left = [0,0] #Defining initial pixel locations of edges along foam stream
low_right = [0,0]
high_left = [1000,1000]
high_right = [1000,1000]

mid_point = 413 #x-axis approx midpoint of stream
top_bar = 210 #y-axis, defining threshold bars within image  
bottom_bar = 450 #y-axis value

left_x = 175
right_x = 600

foam_up = 0
#***********************************************************************
#******************************Main Code********************************
#***********************************************************************

#background subtraction setup
bkgnd = cv2.bgsegm.createBackgroundSubtractorMOG() 
#bkgnd = cv2.bgsegm.createBackgroundSubtractorGMG() 

#bkgnd = cv2.createBackgroundSubtractorMOG2()
camera = cv2.VideoCapture('/home/odroid/Desktop/python_scripts/test/test_images/Edited_Foam_Dispense_Short.mp4')

#runonce = 0

#while(runonce <=8):
while(True):
	(grabbed, frame) = camera.read()
		
	#applying background subtraction ... with learning rate to only use 
	#first frame of video stream	
	
	img_sub = bkgnd.apply(frame, 10, learningRate = 0.001)
	#img_sub = bkgnd.apply(frame, 6, .005)
		
	#Canny Edge Detection
	canny_threshold = cv2.Canny(img_sub, CANNY_LOWER_BOUND, CANNY_UPPER_BOUND)	
	
	#Hough Lines 
	hlines = cv2.HoughLinesP(canny_threshold, HOUGH_RHO, HOUGH_THETA, MIN_LINE_LENGTH, MAX_LINE_GAP)
	
	#in this code... the first frame processed returns a HoughLines array 
	#of 'None'
	#lines: a vector that stores the parameters (x_start, y_start, x_end, y_end) 
	#of the detected lines
	#ie, a point will look like [348, 159, 348, 159]
	
	if hlines is None: #in case HoughLinesP fails to return a set of lines
		hlines = np.array([[0,0,0,0]])
	
	#This draws the line on the image	
	else:
		for l in hlines:
			leftx, boty, rightx, topy = l[0]
			cv2.line(frame, (leftx, boty), (rightx, topy), (0, 255, 0), 2)
	
	
	#  This needs to be adjusted so that it doesn't display a line if there's no stream ... currently it persists
	if len(hlines.shape) == 3 :
		a,b,c = hlines.shape
		for j in range(a):
			if hlines[j][0][0] > left_x and hlines[j][0][2] < right_x : #providing bounding box on left and right
				if hlines[j][0][1] > top_bar and hlines[j][0][1] < bottom_bar and hlines[j][0][0] < mid_point: #bounding on the left ... below a certain height
					if high_left[1] >= np.max(hlines[j][0][1]):
						high_left[0] = hlines[j][0][0]
						high_left[1] = hlines[j][0][1]
			
					if low_left[1] <= np.max(hlines[j][0][1]):
						low_left[0] = hlines[j][0][0]
						low_left[1] = hlines[j][0][1]
				
				if hlines[j][0][1] > top_bar and hlines[j][0][1] < bottom_bar and hlines[j][0][0] > mid_point: #bounding on the right ... below a certain height
					if high_right[1] >= np.max(hlines[j][0][1]):
						high_right[0] = hlines[j][0][0]
						high_right[1] = hlines[j][0][1]
			
					if low_right[1] <= np.max(hlines[j][0][1]):
						low_right[0] = hlines[j][0][0]
						low_right[1] = hlines[j][0][1]
		
		#change this so it's a moving average with decay?	
		#qconsider exponential decay moving average
		
		if abs(high_left[0]-low_left[0]) < 30 and abs(high_right[0]-low_right[0]) < 30:
				foam_up = 0
		else:
			foam_up = 1 
		
		cv2.line(frame, (high_right[0],high_right[1]),(low_right[0],low_right[1]), (255,0,255), 3)
		cv2.line(frame, (high_left[0],high_left[1]),(low_left[0],low_left[1]), (255,0,255), 3)
		#cv2.line(frame, (413,0),(413,700), (255,0,0),3) #midpoint
		cv2.line(frame, (175,0),(175,700), (255,0,0),3) #lower x-bound
		cv2.line(frame, (600,0),(600,700), (255,0,0),3) #upper x-bound
		
		#cv2.imshow('background subtraction', img_sub)
		#file = "/home/odroid/Desktop/python_scripts/test/test_images/background_subtraction.png"
		#cv2.imwrite(file, img_sub)
		#cv2.imshow('canny_threshold', canny_threshold)
		#cv2.imshow(title, frame)
		cv2.imshow("frame", frame)
		print(foam_up)
	
	#runonce = 1 + runonce
	
	#print(runonce)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

camera.release()
cv2.destroyAllWindows()
