import numpy as np
import cv2 as cv
import sys

haar_cascade= cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

people = ["Henok"]

video = cv.VideoCapture(0)
video.set(3,640)
video.set(4,480)

conf = 0

while True:
    success, img = video.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    face_rect = haar_cascade.detectMultiScale(gray,1.1,4)

    for (x, y, w, h) in face_rect:
        face_roi = gray[y: y + h, x: x + w]

        label, confidence = face_recognizer.predict(face_roi)
        conf = confidence

        text = str(people[label]) + " " +str(round(confidence)) + "%"
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),1)
        if confidence >= 0:
            cv.putText(img,text,
            (x+(w//2)-10,y+(h//2)-10),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),1)
    
    cv.imshow("face",img)


    if cv.waitKey(1) & 0xFF == ord('q'):
        print(conf)
        sys.exit("success")
    

