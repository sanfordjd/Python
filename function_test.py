#Joe Sanford
#MAY2017

#Playing with functions

import cv2
import numpy as np
import imutils

#word = "text to screen"



while(True):

	a("text to screen")

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()


def a(word):
	print(word)
