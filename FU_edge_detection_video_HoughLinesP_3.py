#Joe Sanford
#MAY 2017

########################################################################
# This version checks if the foam components are being extruded first
# using cve.findContours ... then checks for foam up condition
# Algorithm:
# 	Color Mask
#   Erode Mask
# 	Dilate Mask
#   Canny Edge Detection
#	findContours
#   if Contours-> HoughLinesP
#		find highest and lowest points that are left and right of the 
#			midpoint
#		Check difference in x coordinates of the highest and lowest 
#			points
#		Output if foam_up or not ... with some degrading factor
########################################################################

########################################################################
# Imports
########################################################################
import cv2
import numpy as np
import imutils
import time
########################################################################
# Parameters
########################################################################
sensitivity = 5
whiteLower = ( 0, 0, 255 - sensitivity) #fiddle with these values some more
whiteUpper = ( 255, sensitivity, 255)

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
top_bar = 90 #y-axis, defining threshold bars within image  
bottom_bar = 400 #y-axis value

left_x = 175 #look only between these points ... may be able to get rid
right_x = 600 #of this

foam_up = 0

camera = cv2.VideoCapture('/home/odroid/Desktop/python_scripts/test/test_images/Edited_Foam_Dispense_Short.mp4')
last_frame = time.time()
time_per_frame = []

########################################################################
# Main Loop
########################################################################

while(True):
	(grabbed, frame) = camera.read()
	if grabbed == True:
			
		#frame = imutils.resize(frame, width = 600)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			
		mask = cv2.inRange(hsv, whiteLower, whiteUpper)
		mask = cv2.erode(mask, None, iterations = 2 )
		mask = cv2.dilate(mask, None, iterations = 2 )
		
		#Canny Edge Detection
		canny_threshold = cv2.Canny(mask, CANNY_LOWER_BOUND, CANNY_UPPER_BOUND)	
		
		#Contours - finding contours of shape based on Canny Edge Detection		
		image, contours, hierarchy = cv2.findContours(canny_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		
		if contours == []:
			print('End of Video File')
			break		
		else:
			cnt = contours[0]
			area = cv2.contourArea(cnt)
			#drawing contour
			image_contour = cv2.drawContours(frame,contours, -1, (0,255,0), 2)
			cv2.imshow('contours', image_contour)
					
			#we only want those HoughLinesP for when the stream is on
			if area > 20000:
				#Hough Lines 
				hlines = cv2.HoughLinesP(canny_threshold, HOUGH_RHO, HOUGH_THETA, MIN_LINE_LENGTH, MAX_LINE_GAP)
				
				#in this code... the first frame processed returns a HoughLines array 
				#of 'None'
				#lines: a vector that stores the parameters (x_start, y_start, x_end, y_end) 
				#of the detected lines
				#ie, a point will look like [348, 159, 348, 159]
		
				if hlines is None: #in case HoughLinesP fails to return a set of lines
					hlines = np.array([[0,0,0,0]])
				
				#  This needs to be adjusted so that it doesn't display a line if there's no stream ... currently it persists
				#This draws the line on the image	
				else:
					for l in hlines:
						leftx, boty, rightx, topy = l[0]
						cv2.line(frame, (leftx, boty), (rightx, topy), (0, 255, 0), 2)
								
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
									
						cv2.line(frame, (high_right[0],high_right[1]),(low_right[0],low_right[1]), (255,0,255), 3)
						cv2.line(frame, (high_left[0],high_left[1]),(low_left[0],low_left[1]), (255,0,255), 3)
					#we are assuming a 15FPS capture rate ... and we want a "detected foam" 
					#to go away if there's no foam up detected for 1 sec.
					
					if abs(high_left[0]-low_left[0]) < 30 and abs(high_right[0]-low_right[0]) < 30:
						if foam_up > 0 :
							foam_up = foam_up - (1/15)
							
					else:
						foam_up = 1 
					
					print(foam_up)
				#cv2.imshow('frame', frame)
			
	if grabbed == False:
		print('Error Reading Video File')
		break
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

time_per_frame.append(time.time()-last_frame)
last_frame = time.time()

camera.release()
cv2.destroyAllWindows()

fps = 1/np.average(time_per_frame)
print 'Average Frames Per Second: ', fps
