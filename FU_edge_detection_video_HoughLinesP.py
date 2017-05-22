#Joe Sanford
#APR 2017
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

mid_point = 420 #x-axis approx midpoint of stream ... automate eventually
top_bar = 210 #y-axis, defining threshold bars within image  
bottom_bar = 450 #y-axis value

bkgnd = cv2.bgsegm.createBackgroundSubtractorMOG()

#bkgnd = "/home/odroid/Desktop/python_scripts/test/test_images/background_image.png"
cap = cv2.VideoCapture('/home/odroid/Desktop/python_scripts/test/test_images/Edited_Foam_Dispense_Short.mp4')
file_loc = "/home/odroid/Desktop/python_scripts/test/test_images/background_image.png"
success, image = cap.read()
cv2.imwrite(file_loc, image)

T = True

while(T != False):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
    

	##background subtraction
	img_sub = bkgnd.apply(frame)
		
	##convert to grayscale
	##img_sub_gray_image = cv2.cvtColor(img_sub, cv2.COLOR_BGR2GRAY)
	##thresholding, forcing to binary image
	#ret,threshold1 = cv2.threshold(img_sub, LOWER_BOUND, UPPER_BOUND, cv2.THRESH_BINARY)
	##ret,threshold1 = cv2.threshold(img_sub_gray_image, LOWER_BOUND, UPPER_BOUND, cv2.THRESH_BINARY)

	##running Canny Edge Detection
	#canny_threshold1 = cv2.Canny(threshold1, CANNY_LOWER_BOUND, CANNY_UPPER_BOUND)
	#cv2.imshow('title', canny_threshold1)
	
	##finding HoughLines
	#hlines = cv2.HoughLinesP(canny_threshold1, HOUGH_RHO, HOUGH_THETA, MIN_LINE_LENGTH, MAX_LINE_GAP)

	#if hlines is not None:

		#a,b,c = hlines.shape
		#for i in range(a):
			#cv2.line(img, (hlines[i][0][0], hlines[i][0][1]), (hlines[i][0][2], hlines[i][0][3]), (0,255,0), 3, cv2.LINE_AA)
	##lines: a vecotr that stores the parameters (x_start, y_start, x_end, y_end) of the detected lines
	##ie, a point will look like [348, 159, 348, 159]

		#for j in range(a):
			#if hlines[j][0][1] > top_bar and hlines[j][0][1] < bottom_bar and hlines[j][0][0] < mid_point:
				#if high_left[1] >= np.max(hlines[j][0][1]):
					#high_left[0] = hlines[j][0][0]
					#high_left[1] = hlines[j][0][1]

				#if low_left[1] <= np.max(hlines[j][0][1]):
					#low_left[0] = hlines[j][0][0]
					#low_left[1] = hlines[j][0][1]
		
			#if hlines[j][0][1] > top_bar and hlines[j][0][1] < bottom_bar and hlines[j][0][0] > mid_point:
				#if high_right[1] >= np.max(hlines[j][0][1]):
					#high_right[0] = hlines[j][0][0]
					#high_right[1] = hlines[j][0][1]

				#if low_right[1] <= np.max(hlines[j][0][1]):
					#low_right[0] = hlines[j][0][0]
					#low_right[1] = hlines[j][0][1]
				
		#if abs(high_left[0]-low_left[0]) < 30 and abs(high_right[0]-low_right[0]) < 30:
			#title = 'Good Dispense of Foam.'
		#else:
			#title = 'Possible Foam-Up. Clean Nozzle'	
	
		#cv2.line(img, (high_right[0],high_right[1]),(low_right[0],low_right[1]), (255,0,255), 3)
		#cv2.line(img, (high_left[0],high_left[1]),(low_left[0],low_left[1]), (255,0,255), 3)
		#cv2.imshow(title, img)		
	#else:
		#print 'There are no Lines to Detect!'
		#T = False

	
cap.release()
cv2.destroyAllWindows()	
