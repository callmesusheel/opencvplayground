import cv2
import sys

# http://www.learnopencv.com/non-photorealistic-rendering-using-opencv-python-c/

img = cv2.imread(sys.argv[1])
# img = cv2.stylization(img, sigma_s=60, sigma_r=0.01)
img = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.6)
# gray, img = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
img = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)

cv2.imshow('stylize', img)

k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()