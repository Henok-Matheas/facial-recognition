import cv2 as cv
import sys
import os





video = cv.VideoCapture(0)
video.set(3,640)
video.set(4,480)

name = input("your name?")


try:
    path = os.mkdir(os.path.join("./images",name))
    people_file = open(r"people.txt","w")
    written_name = name + " "
    people_file.write(written_name)
    people_file.close()
except:
    print("already exists")
    path = os.path.join("./images",name)

count = 1
while count <= 1000 :
    subject = path + "/img" + str(count) + ".jpg"
    sucess, img = video.read()
    copy = img.copy()
    cv.imshow("wee",img)
    cv.imwrite(subject,copy)
    count += 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        sys.exit("success")

print('photos for training model have been taken successfully!!')