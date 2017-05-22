import cv2
import numpy as np
import argparse
import glob

img = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/screenshot_test.png')

sigma = 0.33

v = np.median(img)
	
lower = int(max(0, (1.0-sigma)*v))
upper = int(min(255, (1.0+sigma)*v))
edges_auto = cv2.Canny(img,lower,upper)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges_wide = cv2.Canny(gray_image, 10, 250)

	
cv2.imshow('edges auto', edges_auto)
cv2.imshow('edges wide', edges_wide)


cv2.waitKey(0)
	
