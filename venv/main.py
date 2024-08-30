import os
import pickle
import face_recognition
import cv2
import numpy as np
import cvzone

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4,480)

imgBackground = cv2.imread("../resources/background.png")

# importing the photo
folderPath = "../resources/Modes"
modePath = os.listdir(folderPath)
imgModeList = []

for path in modePath:
    imgModeList.append(cv2.imread(os.path.join(folderPath,path))) # add photo in mode path

#load file mã hóa
file=open("encode-file.p", "rb")
encodeListWithIds = pickle.load(file)
encodeListKnown, studentIds = encodeListWithIds
file.close()
# print(encodeListKnown)
# xong...


while True:
    ret, frame = cap.read()

    imgS = cv2.resize(frame, (0,0), None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)  # chuyển từ BGR san RGB

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

    imgBackground[162: 162 + 480, 55 : 55 + 640] = frame
    imgBackground[44: 44+ 633, 808 : 808 + 414] = imgModeList[3]

    for enFace, faceloc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,enFace)
        faceDis = face_recognition.face_distance(encodeListKnown,enFace)
        matchIndex = np.argmin(faceDis)
        # print(matchIndex)
        if matches[matchIndex]:
            y1,x2,y2,x1 = faceloc
            y1,x2,y2,x1 = y1*4, x2*4, y2*4,x1 *4
            bbox = 55 + x1, 162 + y1,x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt = 0)
    cv2.imshow("Cam:", imgBackground)
    if(cv2.waitKey(1)  == ord(" ")) :break


