import cv2
import numpy as np
from os import listdir
from os.path import isfile , join

data_path='C:/Users/HP/PycharmProjects/face_detection/facefolder/'
# onlyfiles= [f for f in listdir(data_path) if isfile(join(data_path))]

onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
onlyfiles = onlyfiles [1:]

Traning_Data, Labels=[],[]

for i, files in enumerate(onlyfiles):
    image_path=data_path + onlyfiles[i]
    images = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    Traning_Data.append(np.asanyarray(images,dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels,dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Traning_Data), np.asarray(Labels))

print("dataset model training completed")

