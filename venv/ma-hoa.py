
import cv2
import face_recognition
import pickle
import os

# importing student images
folderPath = "../image/"
modePath = os.listdir(folderPath)
imgList = []
stIds = []

for path in modePath:
    imgList.append(cv2.imread(os.path.join(folderPath,path))) # add photo in mode path
    stIds.append(os.path.splitext(path)[0])

    fileName = os.path.join(folderPath,path)


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

