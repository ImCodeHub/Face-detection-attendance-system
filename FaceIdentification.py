from ast import Str
from cgitb import text
import imp
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tokenize import String
from turtle import radians, title, width
from PIL import Image, ImageTk
import cv2 as cv
import os
import mysql.connector
from time import strftime
from datetime import datetime


class faceRecognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management system")
        self.root.geometry("1920x1080+0+0")
        self.root.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')

    # =========background image=======
        bgImage = Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\FR4.jpg')
        self.bg = ImageTk.PhotoImage(bgImage)
        background = Label(self.root, image=self.bg)
        background.place(x=0, y=0)

        Title = Label(background, text="Face Recognistion", font=(
            'arial', 50, 'bold'), fg="white", bg='#1b172b')
        Title.place(x=100, y=30)
    # ===============button=============

        btn = Button(background, text='Face Recognition', command=self.faceRecog,
                     cursor='hand2', font=('arial', 25, font.BOLD), bg='#383836', fg='white')
        btn.place(x=680, y=368, width='300', height='100')

    # ==========Attendance===========    
    def markAttendance(self,i,r,n,d):
        with open(r'D:\MyPythonProgramming\Face detection attendance system\AttendanceReport\Attendance.csv','r+',newline='\n') as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry=line.split((','))   # to seperate the value
                nameList.append(entry[0])
            if ((i not in nameList)) and ((r not in nameList)) and ((n not in nameList)) and ((d not in nameList)):
                now=datetime.now()
                d1=now.strftime('%d/%m/%Y')
                dtString=now.strftime('%I:%M:%S')
                f.writelines(f'{i},{r},{n},{d},{dtString},{d1},Present\n')






    # ==========face recognition=========
    def faceRecog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            grayImage = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(grayImage, scaleFactor, minNeighbors)

            coord = []

            for(x, y, w, h) in features:
                cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(grayImage[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                print(id)
                 
                conn = mysql.connector.connect(user='root', password='password', host='localhost', database='testdb')

                MyCursor = conn.cursor()
                MyCursor.execute('select StudentName from facerecognition where StudentID='+str(id))
                n = MyCursor.fetchone()
                n = "+".join(n)

                MyCursor.execute('select RollNo from facerecognition where StudentID='+str(id))
                r = MyCursor.fetchone()
                r = "+".join(r)

                MyCursor.execute('select Department from facerecognition where StudentID='+str(id))
                d = MyCursor.fetchone()
                d = "+".join(d)

                MyCursor.execute('select StudentID from facerecognition where StudentID='+str(id))
                i = MyCursor.fetchone()
                i = "+".join(i)

                if confidence > 82:
                    cv.putText(img, f"Student ID:{i}", (x, y-110), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv.putText(img, f"Roll No:{r}", (x, y-80), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv.putText(img, f"Name:{n}", (x, y-50), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv.putText(img, f"Department:{d}", (x, y-20), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.markAttendance(i,r,n,d)
                else:
                    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv.putText(img,"Unknown Face", (x, y-20),cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),'Face',clf) 
            return img

        faceCascade = cv.CascadeClassifier(r'D:\MyPythonProgramming\Face detection attendance system\haarcascade_frontalface_alt.xml')
        clf = cv.face.LBPHFaceRecognizer_create()
        clf.read(r'D:\MyPythonProgramming\Face detection attendance system\classifier.xml')

        VideoCap = cv.VideoCapture(0)
        # if not VideoCap.isOpened():
        #     print("Cannot open camera")
        #     exit()

        while True:
            ret,image = VideoCap.read()
            # if not ret:
            #     print("Can't receive frame (stream end?). Exiting ...")
            #     break
            image = recognize(image, clf, faceCascade)
            cv.imshow('Welcome to the Face recognition', image)

            if cv.waitKey(1) == 13:
                break
        VideoCap.release()
        cv.destroyAllWindows()  


if __name__ == "__main__":
    root = Tk()
    app = faceRecognition_System(root)
    root.mainloop()
