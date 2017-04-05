import numpy as np
import cv2
import sys
 
img = cv2.imread(sys.argv[1])
mask = np.zeros(img.shape[:2],np.uint8)

cascPath = 'haarcascade_frontal_face.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw a rectangle around the faces
cropImg = None
for (x, y, w, h) in faces:
  bgdModel = np.zeros((1,65),np.float64)
  fgdModel = np.zeros((1,65),np.float64)
   
  # rect = (x,y,x+w, y+h)
  # cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
  
  # mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
  # img = img*mask2[:,:,np.newaxis]

  rect = (x-40,y-40,x+(3*w), y+(3*h))
  cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

  mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
  img = img*mask2[:,:,np.newaxis]


 
cv2.imshow('Video', img)

k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()