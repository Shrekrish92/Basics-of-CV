import os
import cv2 as cv
import numpy as np

ppl = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

haar_cascade= cv.CascadeClassifier('haar_face.xml')

DIR = r'/Users/shreyakrishna/Downloads/opencv-course-master/Resources/Faces/train'

feature=[]
labels=[]

def create_train():
    for person in ppl:
        path=os.path.join(DIR, person)
        label = ppl.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w]
                feature.append(faces_roi)
                labels.append(label)
create_train()
print("Training Done!! ---------------------")

feature= np.array(feature, dtype='object')
labels=np.array(labels)

face_recogniser = cv.face.LBPHFaceRecognizer_create()

face_recogniser.train(feature,labels)

face_recogniser.save('face_trained.yml')
np.save('features.npy',feature)
np.save('labels.npy',labels)