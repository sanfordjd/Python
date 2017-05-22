import cv2
import numpy as np

img = cv2.imread('/home/odroid/Desktop/python_scripts/test/test_images/screenshot_test.png')
#gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray_image, 10, 250)
#cv2.imshow('edges', edges)

kernel_sharpen_1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
#kernel_sharpen_2 = np.array([[-1,-1,-1,-1,-1],
							 #[-1,2,2,2,-1],
							 #[-1,2,8,2,-1],
							 #[-1,2,2,2,-1],
							 #[-1,-1,-1,-1,-1]]) / 8.0

#kernel_sharpen_2 = np.array([[-1,-1,-1],[-1,7,-1],[-1,-1,-1]])

#kernel_sharpen_3 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

kernel_emboss = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])

output_0 = cv2.filter2D(img, -1, kernel_sharpen_1)
#output_1 = cv2.filter2D(gray_image, -1, kernel_sharpen_1)
#output_2 = cv2.filter2D(gray_image, -1, kernel_sharpen_2)
#output_3 = cv2.filter2D(gray_image, -1, kernel_sharpen_3)
output_em = cv2.filter2D(img, -1, kernel_emboss)

#cv2.imshow('gray', gray_image)
cv2.imshow('sharpen0', output_0)
#cv2.imshow('sharpen1', output_1)
#cv2.imshow('sharpen2', output_2)
#cv2.imshow('sharpen3', output_3)
cv2.imshow('emboss', output_em)

edges_sharpen_0 = cv2.Canny(output_0, 10, 250)
#edges_sharpen_1 = cv2.Canny(output_1, 10,
#edges_sharpen_3 = cv2.Canny(output_3, 10, 250)
edges_emboss = cv2.Canny(output_em, 10, 250)

#cv2.imshow('edges', edges)
cv2.imshow('edgessharpen0', edges_sharpen_0)
#cv2.imshow('edgessharpen1', edges_sharpen_1)
#cv2.imshow('edgessharpen3', edges_sharpen_3)
cv2.imshow('edgesemboss', edges_emboss)

added_img = edges_sharpen_0 + edges_emboss

cv2.imshow('added together', added_img)

cv2.waitKey(0)
