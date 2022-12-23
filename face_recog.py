import cv2 as cv
import numpy as np

ppl = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
haar_cascade= cv.CascadeClassifier('haar_face.xml')

# features =  np.load('features.npy')
# labels = np.load('labels.npy')

face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.read('face_trained.yml')

img = cv.imread(r'/Users/shreyakrishna/Downloads/opencv-course-master/Resources/Faces/val/mindy_kaling/3.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_ben', gray)

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

for (x,y,w,h) in face_rect:
    face_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recogniser.predict(face_roi)
    print(f'label = {ppl[label]} with confidence of {confidence}')

    cv.putText(img, str(ppl[label]), (20,20), cv.FONT_HERSHEY_PLAIN, 1.0, (0,255,0), thickness=1)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('detected face', img)

cv.waitKey(0)