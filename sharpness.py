import cv2
import sys
import numpy as np

img = cv2.imread(sys.argv[1])
cv2.imshow('Original', img)

# http://stackoverflow.com/questions/32454613/python-unsharp-mask (except changed the value from -0.5 to 0.0)

# http://docs.opencv.org/trunk/d6/d00/tutorial_py_root.html

gaussian_3 = cv2.GaussianBlur(img, (9,9), 10.0)
unsharp_image = cv2.addWeighted(img, 1.4, gaussian_3, 0.0, 0, img)
cv2.imshow('Unsharp Mask', unsharp_image)


img = cv2.imread(sys.argv[1])
gaussian_3 = cv2.GaussianBlur(img, (9,9), 10.0)
unsharp_image = cv2.addWeighted(img, 1.4, gaussian_3, 0.0, 0, img)
cv2.imshow('Unsharp Mask 2', unsharp_image)


######### TRY THIS #########

# http://docs.opencv.org/trunk/d1/d5c/tutorial_py_kmeans_opencv.html #

############################

k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()