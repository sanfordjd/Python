import cv2
import numpy as np
import imutils 
import argparse

np.set_printoptions(threshold=np.inf) #to print entire array, no truncation

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "/home/odroid/Desktop/python_scripts/test/test_images/Edited_Foam_Dispense_Short.mp4")

args = vars(ap.parse_args())

LOWER_BOUND = 55   #cv2.threshold()
UPPER_BOUND = 255  #cv2.threshold()

CANNY_LOWER_BOUND = 10  #cv2.Canny()
CANNY_UPPER_BOUND = 250 #cv2.Canny()

MIN_LINE_LENGTH = 2  #HoughLinesP()
MAX_LINE_GAP = 100     #HoughLinesP() 
HOUGH_THETA = np.pi/180 #HoughLinesP() angle resolution of the accumulator, radians
HOUGH_THRESHOLD = 25 #HoughLinesP() 
HOUGH_RHO = 1         #HoughLinesP() rho, Distance resolution of the accumulator, pixels


bkgnd = cv2.bgsegm.createBackgroundSubtractorMOG()
camera = cv2.VideoCapture('/home/odroid/Desktop/python_scripts/test/test_images/Edited_Foam_Dispense_Short.mp4')

# if a video path was not supplied, grab the reference
# to the webcam
#if not args.get("video", False):
#	camera = cv2.VideoCapture(0)
#	print("Video file not grabbed")

# otherwise, grab a reference to the video file
#else:
#	camera = cv2.VideoCapture(args["video"])

while(True):
	(grabbed, frame) = camera.read()
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if args.get("video") and not grabbed:
		break
		
	# resize the frame, blur it, and convert it to the HSV
	# color space
	#frame = imutils.resize(frame, width=600)
	
	img_sub = bkgnd.apply(frame)#, learningRate = 0.001)
	#img_sub = bkgnd.apply(frame)
	#cv2.imshow('img_sub', img_sub)
	
	#canny_threshold = cv2.Canny(frame, CANNY_LOWER_BOUND, CANNY_UPPER_BOUND)	
	canny_threshold = cv2.Canny(img_sub, CANNY_LOWER_BOUND, CANNY_UPPER_BOUND)	
	
	#cv2.imshow('canny_threshold', canny_threshold)
	
	hlines = cv2.HoughLinesP(canny_threshold, HOUGH_RHO, HOUGH_THETA, MIN_LINE_LENGTH, MAX_LINE_GAP)
	
	print(hlines)
	print(hlines.shape)
	
	#a,b,c = hlines.shape
	
	#for k in range(a):
		#print(hlines.shape)
		#break
		#cv2.line(frame, (hlines[k][0][0], hlines[k][0][1]), (hlines[k][0][2], hlines[k][0][3]), (0,255,0), 3, cv2.LINE_AA)
	#	print("getting hlines")
	#	break
	
	
	cv2.imshow("frame", frame)
	
		
	
	
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

camera.release()
cv2.destroyAllWindows()
