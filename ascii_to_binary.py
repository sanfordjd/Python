#Joe Sanford
#MAY02017
# This script will import a text file, read it, convert it to binary
# and output a series of binary images

import numpy as np
import cv2
import imutils
import sys

text1 = open("filename.text", "r")
letters = text1.read()

a = len(letters)

binary_text = [None]*a #pre-allocating a list
#for j in range(a):
#for letter in letters:
		#binary_text[j] = (bin(ord(letter))[2:].zfill(8))
		#print(binary_text[j])
print('test')
print(' '.join([bin(ord(letter))[2:].zfill(8) for letter in letters]))
		#sys.stdout.write(binary_text[j])
		#sys.stdout.flush()

#print(binary_text[0:140])
#print(binary_text[0])

#and then create a series of loops that convert from binary to the 
#images 
