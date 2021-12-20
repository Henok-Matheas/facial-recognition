import cv2 as cv
import sys
import os




video = cv.VideoCapture(0)
video.set(3,640)
video.set(4,480)

name = input("your name?")

try:
    os.mkdir(name)
except:
    print("already exists")

count = 101
while count <= 200 :
    subject = name + "/img" + str(count) + ".jpg"
    sucess, img = video.read()
    copy = img.copy()
    cv.imshow("wee",img)
    cv.imwrite(subject,copy)
    count += 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        sys.exit("success")

# sys.exit()