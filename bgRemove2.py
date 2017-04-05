import numpy as np
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

#Load the Image
img = cv2.imread(sys.argv[1],1)

fgbg = cv2.createBackgroundSubtractorMOG2()

#Create a mask holder
fgmask = fgbg.apply(frame)
 
cv2.imshow('fgmask',frame)
cv2.imshow('frame',fgmask)


k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
    