import cv2 as cv
import os
import numpy as np


DIR = "/home/henok/Desktop/Training/AI"
people = ["Henok"]

features = []
labels = []

haar_cascade= cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')


def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = person.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)

            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray,1.1,4)

            for (x,y,w,h) in face_rect:
                face_roi = gray[y: y + h, x: x + w]
                features.append(face_roi)
                labels.append(label)

create_train()

# print(f"the length of features is {len(features)}")
# print(f"the length of labels is {len(labels)}")

features = np.array(features ,dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy',features)



