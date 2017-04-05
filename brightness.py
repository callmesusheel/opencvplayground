import cv2
import sys
import numpy as np

# http://www.learnopencv.com/non-photorealistic-rendering-using-opencv-python-c/

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)


img = cv2.imread(sys.argv[1])
original = img
img = adjust_gamma(img, 1.5)

cv2.imshow('original', original)
cv2.imshow('result', img)

k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()