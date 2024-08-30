from fileinput import filename

import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from firebase_admin.storage import bucket

cred = credentials.Certificate("../serviceAccountKey.json") #json
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://test-data-base-da118-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "test-data-base-da118.appspot.com" # ket noi voi storage của fibase
})

# importing student images
folderPath = "../image"
modePath = os.listdir(folderPath)
imgList = []
stIds = []

for path in modePath:
    imgList.append(cv2.imread(os.path.join(folderPath,path))) # add photo in mode path
    stIds.append(os.path.splitext(path)[0])

    fileName = os.path.join(folderPath,path)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

# print(stIds)

# mã hóa
def findEncode(imgList):
    ecodeList = []
    for img in imgList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # chuyển từ BGR san RGB
        endcode = face_recognition.face_encodings(img)[0]
        ecodeList.append(endcode)
    return ecodeList


ecList = findEncode(imgList) # ảnh được mã hóa
ecWithKnown = [ecList, stIds]
# print("complete")
# print(ecWithKnown)
file = open("encode-file.p", 'wb') # file chứa ảnh mã hóa

pickle.dump(ecWithKnown, file)

file.close()

