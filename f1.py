import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo, showerror
from os import listdir
import requests
from os.path import isfile, join
import csv
from csv import reader
import tkinter

# ---------------------------------------------> FUNCTION TO SEND SMS....
def sms(name,time):

    url = "https://www.fast2sms.com/dev/bulk"
    querystring = {"authorization":"NLieK4M0ENVgqwuZKCzyHF1zrHuDLoNJaCfHnetZABdPqYPoEgj5PcswWWSo",
                   "sender_id":"FSTSMS",
                   "message":"WARNING !!!... "+name+"have been seen at time"+time+" .",
                   "language":"english",
                   "route":"p",
                   "numbers":"7415640671"}
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

# --------------------------------------------> FUNCTIO+-N TO RECONISE FACE AND SAVE NAME IN .CSV
def reco():
    path = 'ImagesAttendance'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = [] # it will have all the encode point of the images
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    #-------------------------------------------------> FUNCTION TO SAVE NAME IN .CSV FILE
    def culprit(name):
        with open('culprit_list.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []

            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

    # markAttendance('elon')
    # #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
    # # def captureScreen(bbox=(300,300,690+300,530+300)):
    # #     capScr = np.array(ImageGrab.grab(bbox))
    # #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    # #     return capScr
    #
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0,51,51), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                culprit(name)

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == 13:
            break
    cap.release()
    cv2.destroyAllWindows()
    with open('culprit_list.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                if len(row) != 0:
                    name = row[0]
                    time = row[1]
                    print(name, time)
                    sms(name, time)
#----------------------------------------------------->LOGIN CODE

master = tkinter.Tk()
master.geometry("390x350")
flag = 0

def login():
    if lblpassword.get() == "1" and lblusername.get()=="1":
        reco()
    else:
        print("access denied")


bg_color = "DeepSkyBlue2"
fg_color = "#383a39"
master.configure(background=bg_color)
master.title("Welcome")

# -------username
tkinter.Label(master, text="Username:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=8, padx=(50, 0),                                                                                 pady=(20, 10))
lblusername = tkinter.Entry(master)
lblusername.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))

# ----password
tkinter.Label(master, text="Password:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=9, padx=(50, 0),                                                                                   pady=(20, 10))
lblpassword = tkinter.Entry(master)
lblpassword.grid(row=9, column=1, padx=(10, 10), pady=(20, 10))

# --------button
tkinter.Button(master, text="Login", borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width=15,
               command=login).grid(row=10, padx=(50, 0), pady=(20, 10))

master.mainloop()

# ------------------->

# with open('culprit_list.csv', 'r') as read_obj:
#     csv_reader = reader(read_obj)
#     header = next(csv_reader)
#     if header != None:
#         for row in csv_reader:
#             if len(row) != 0:
#                 name = row[0]
#                 time = row[1]
#                 print(name,time)
#                 # sms(name,time)