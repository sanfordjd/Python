import cv2
import numpy as np

np.arange(20)
x = np.array([[[ 0, -1, 2, 3, 4],
               [ 5, 6, 7, 8, 9],
               [10,11,25,13,14],
               [15,16,17,18,22]],
              
              [[20,18,17,16,15],
               [14,13,12,11,10],
               [ 9, -2, 7, 6, 5],
               [ 4, 3, 2, 1, 0]]])

#arrays in python are zero indexed
#this corresponds to the last row, last column... ie 19
print(x[0])

a,b,c = x.shape
lrg = 0
small = 1000
for i in range(a):
	if lrg <= np.max(x[i]):
	   lrg = np.max(x[i])
		
	if small >= np.min(x[i]):	
	   small = np.min(x[i])
	
	
print(lrg)
print(small)



cv2.waitKey(0)

