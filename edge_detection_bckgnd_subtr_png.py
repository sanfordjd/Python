import cv2
import numpy as np

img = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/test.png')
bkgnd = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/test_background.png')

img_sub = cv2.subtract(img, bkgnd)

cv2.imshow('img color', img)
cv2.imshow('bkgnd color', bkgnd)
cv2.imshow('img_sub', img_sub)

img_sub_gray_image = cv2.cvtColor(img_sub, cv2.COLOR_BGR2GRAY)
cv2.imshow('Subtracting Color Images, made Grayscale', img_sub_gray_image)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_bkgnd = cv2.cvtColor(bkgnd, cv2.COLOR_BGR2GRAY)

img_sub_gray_sub = cv2.subtract(gray_img, gray_bkgnd)
cv2.imshow('Subtracting Grayscale Images', img_sub_gray_sub)

canny_imgsubgraysub = cv2.Canny(img_sub_gray_sub, 10, 250)
canny_imgsubgrayimage = cv2.Canny(img_sub_gray_image, 10, 250)

cv2.imshow('canny_imgsubgraysub', canny_imgsubgraysub)
cv2.imshow('canny_imgsubgrayimage', canny_imgsubgrayimage)

cv2.waitKey(0)
	
