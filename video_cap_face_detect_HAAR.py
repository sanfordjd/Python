import cv2
import sys
import numpy as np

#cascPath = sys.argv[1] #figure out what this means
#faceCascade = cv2.CascadeClassifier(cascPath)
#faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cascPath = '/home/odroid/Desktop/python_scripts/test/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

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
	#flags = cv2.CASCADE_SCALE_IMAGE is different than most examples
	# use https://github.com/opencv/opencv/blob/master/samples/python/facedetect.py
	
	#drawing a rectangle around the faces
	
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
	cv2.imshow('Video', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
# when everything is done, release the capture

video_capture.release()
cv2.destroyAllWindows()
