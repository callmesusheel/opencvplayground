import cv2
import sys
import logging as log
import datetime as dt

from time import sleep

cascPath = 'haarcascade_frontal_face.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
frame = cv2.imread(sys.argv[1],1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

anterior = 0

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw a rectangle around the faces
cropImg = None
for (x, y, w, h) in faces:
    cropImg = frame[y: y + h, x: x + w]
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 10)

if anterior != len(faces):
    anterior = len(faces)
    log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

# Display the resulting frame
cv2.imshow('Video', frame)
# cv2.imwrite(sys.argv[1]+".face.png",cropImg)

k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()