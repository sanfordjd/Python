import cv2
import numpy as np
import argparse
import glob

#== Parameters =========================================================

BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,1.0) # In BGR format

#== Parameters =========================================================

#-- Read Image ---------------------------------------------------------

img = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/screenshot_test.png')
#gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', gray_image)

#-- Edge Detection -----------------------------------------------------

edges = cv2.Canny(img, CANNY_THRESH_1, CANNY_THRESH_2)
edges = cv2.Canny(gray_image, CANNY_THRESH_1, CANNY_THRESH_2)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)

#-- Moving Threshold ---------------------------------------------------

sigma = 0.33
v = np.median(img)

lower = int(max(0, (1.0-sigma)*v)) # for moving threshold
upper = int(min(255, (1.0+sigma)*v)) # for moving thresholdedges_auto = cv2.Canny(img,lower,upper) #for moving threshold
edges_auto = cv2.Canny(img,lower,upper)
edges_wide = cv2.Canny(gray_image, 10, 250)
	
cv2.imshow('edges auto', edges_auto)
cv2.imshow('edges wide', edges_wide)

#-- Find contours in edges, sort by area -------------------------------

cv2.imshow('edges erode and dilate', edges)

#contour_info []
#contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)







cv2.waitKey(0)
#while(True)
#	k = cv2.waitKey(30) & 0xff
#		if k == ord('q'):
#			break
#		elif k == 27:
#			break
			
# When everything is done, release the capture
#cap.release()
#cv2.destroyAllWindows()	
