#!/usr/bin/env python

import numpy as np
import cv2

#img0 = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/test_image1.png')

img1 = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/Default_Project1.png')

#cv2.imshow('image0', img0)
cv2.imshow('image1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
