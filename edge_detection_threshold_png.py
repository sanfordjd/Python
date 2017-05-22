import cv2
import numpy as np
#from matplotlib import pyplot as plt

LOWER_BOUND = 55
img = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/test.png')
bkgnd = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/test_background.png')

#***********************************************************************
#There is a difference between using a background subtracted image
#and just using the Thresholded Grayscale Image.
#***********************************************************************
#***********************************************************************
# Background Subtracted Image
#***********************************************************************
img_sub = cv2.subtract(img, bkgnd)

img_sub_gray_image = cv2.cvtColor(img_sub, cv2.COLOR_BGR2GRAY)
ret,threshold1 = cv2.threshold(img_sub_gray_image, LOWER_BOUND, 255, cv2.THRESH_BINARY)
ret,threshold3 = cv2.threshold(img_sub_gray_image, LOWER_BOUND, 255, cv2.THRESH_TRUNC)
ret,threshold4 = cv2.threshold(threshold3, 40, 255, cv2.THRESH_BINARY)
canny_threshold1 = cv2.Canny(threshold1, 10, 250)

cv2.imshow('Image', img)
cv2.imshow('Subtracted Image', img_sub)
cv2.imshow('Grayscale Subtracted Image', img_sub_gray_image)
cv2.imshow('Thresholded Image-Subtracted Background', threshold1)
cv2.imshow('Truncated Image-Subtracted Background', threshold3)
cv2.imshow('Thresholded Truncated Image-Subtracted Background', threshold4)
cv2.imshow('Canny Edge of Thresholded Image - Subtracted Background', canny_threshold1)

#***********************************************************************
# Gray Scale Image
#***********************************************************************
#img_gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#ret,threshold2 = cv2.threshold(img_gray_image, LOWER_BOUND, 255, cv2.THRESH_BINARY)
#canny_threshold2 = cv2.Canny(threshold2, 10, 250)

#cv2.imshow('Gray Image', img_gray_image)
#cv2.imshow('Threshold Image - Gray Image',threshold2)
#cv2.imshow('Canny Edge of Thresholded Gray Image', canny_threshold2)

cv2.waitKey(0)
	
