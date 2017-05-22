import cv2
import numpy as np
import imutils 
#from line import Line

np.set_printoptions(threshold=np.inf) #to print entire array, no truncation

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

mid_point = 420 #x-axis approx midpoint of stream
top_bar = 210 #y-axis, defining threshold bars within image  
bottom_bar = 450 #y-axis value

bkgnd = cv2.bgsegm.createBackgroundSubtractorMOG()
camera = cv2.VideoCapture('/home/odroid/Desktop/python_scripts/test/test_images/Edited_Foam_Dispense_Short.mp4')

run_once = 0
while(True):
	(grabbed, frame) = camera.read()
		
	img_sub = bkgnd.apply(frame, learningRate = 0.001)
	
	canny_threshold = cv2.Canny(img_sub, CANNY_LOWER_BOUND, CANNY_UPPER_BOUND)	
	
	hlines = cv2.HoughLinesP(canny_threshold, HOUGH_RHO, HOUGH_THETA, MIN_LINE_LENGTH, MAX_LINE_GAP)
	
	
	if hlines is None: #in case HoughLinesP fails to return a set of lines
		hlines = np.array([[0,0,0,0]])
		#hlines.shape = [1,1,4]
	else:
		for l in hlines:
			leftx, boty, rightx, topy = l[0]
			cv2.line(frame, (leftx, boty), (rightx, topy), (0, 255, 0), 2)
	
	#print(len(hlines.shape), hlines.shape)
	
	if len(hlines.shape) == 3 :
		a,b,c = hlines.shape
		for j in range(a):
			if hlines[j][0][1] > top_bar and hlines[j][0][1] < bottom_bar and hlines[j][0][0] < mid_point:
				if high_left[1] >= np.max(hlines[j][0][1]):
					high_left[0] = hlines[j][0][0]
					high_left[1] = hlines[j][0][1]
		
				if low_left[1] <= np.max(hlines[j][0][1]):
					low_left[0] = hlines[j][0][0]
					low_left[1] = hlines[j][0][1]
			
			if hlines[j][0][1] > top_bar and hlines[j][0][1] < bottom_bar and hlines[j][0][0] > mid_point:
				if high_right[1] >= np.max(hlines[j][0][1]):
					high_right[0] = hlines[j][0][0]
					high_right[1] = hlines[j][0][1]
		
				if low_right[1] <= np.max(hlines[j][0][1]):
					low_right[0] = hlines[j][0][0]
					low_right[1] = hlines[j][0][1]
		
		if abs(high_left[0]-low_left[0]) < 30 and abs(high_right[0]-low_right[0]) < 30:
				title = 'Good Dispense of Foam.'
		else:
			title = 'Possible Foam-Up. Clean Nozzle'
		
		cv2.line(frame, (high_right[0],high_right[1]),(low_right[0],low_right[1]), (255,0,255), 3)
		cv2.line(frame, (high_left[0],high_left[1]),(low_left[0],low_left[1]), (255,0,255), 3)
			
		cv2.imshow('canny_threshold', canny_threshold)
		cv2.imshow("frame", frame)
	
		
	#run_once = run_once + 1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

camera.release()
cv2.destroyAllWindows()
