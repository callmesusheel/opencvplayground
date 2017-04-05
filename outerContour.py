import cv2 
import numpy as np 
import sys

# Read in the image as grayscale - Note the 0 flag
img = cv2.imread(sys.argv[1],-1)
im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# im = cv2.imread(sys.argv[1], 0)

# Run findContours - Note the RETR_EXTERNAL flag
# Also, we want to find the best contour possible with CHAIN_APPROX_NONE
ret, contours, hierarchy = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Create an output of all zeroes that has the same shape as the input
# image
out = np.zeros_like(im)

# On this output, draw all of the contours that we have detected
# in white, and set the thickness to be 3 pixels

# Read into the link below to smoothen the curves
# http://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html
cv2.drawContours(img, contours, -1, (255,204, 204, 204), 5)
cv2.drawContours(img, contours, -1, (255,255, 255, 255), 3)

# Spawn new windows that shows us the donut
# (in grayscale) and the detected contour
cv2.imshow('Donut', img) 
# cv2.imshow('Output Contour', out)

k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
    cv2.imwrite('result.png', img) 