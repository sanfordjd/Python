import cv2
import sys
import numpy as np

#cascPath = sys.argv[1] #figure out what this means
#faceCascade = cv2.CascadeClassifier(cascPath)
#faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

facecascPath = '/home/odroid/Desktop/python_scripts/test/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(facecascPath)

eyecascPath = '/home/odroid/Desktop/python_scripts/test/haarcascades/haarcascade_eye.xml'
eyeCascade = cv2.CascadeClassifier(eyecascPath)

video_capture = cv2.VideoCapture(0)

while True:
	#capture frame by frame
	ret, frame = video_capture.read()
	
	frame = cv2.flip(frame, 1)
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	#faces = cascade.detectMultiScale(
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize = (30, 30),
		flags = cv2.CASCADE_SCALE_IMAGE
	)
	
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x, y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		
		eyes = eyeCascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)

	#flags = cv2.CASCADE_SCALE_IMAGE is different than most examples
	# use https://github.com/opencv/opencv/blob/master/samples/python/facedetect.py
	
	#drawing a rectangle around the faces
	
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
	cv2.namedWindow('Video', cv2.WINDOW_NORMAL)	
	cv2.imshow('Video', frame)
	
	k = cv2.waitKey(30) & 0xff
	if k == ord('q'):
		break
	elif k == 27:
		break
		
# when everything is done, release the capture

video_capture.release()
cv2.destroyAllWindows()
