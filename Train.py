from cgitb import text
import imp
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tokenize import String
from turtle import radians, title, width
from PIL import Image, ImageTk
from numpy import imag, record
import cv2 as cv
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management system")
        self.root.geometry("1920x1080+0+0")
        self.root.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')

    # =========background image=======
        bgImage=Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\StdBackground.jpg')
        self.bg=ImageTk.PhotoImage(bgImage)
        background=Label(self.root,image=self.bg)
        background.place(x=0,y=0)
    # ========Button for Train Data Set=========
        btn=Button(background,text='Train Data Set',command=self.train_Classifier,cursor='hand2',font=('arial',25,font.BOLD),bg='#383836',fg='white')
        btn.place(x=680,y=368,width='300',height='100')


    def train_Classifier(self):
        data_dir=(r'D:\MyPythonProgramming\Face detection attendance system\photosample')
        path=[os.path.join(data_dir,file )for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #convert in grey sacle image 
            imageNp=np.array(img,'uint8')  #convert into grid
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv.imshow('Training',imageNp)
            cv.waitKey(1)==13
        ids=np.array(ids)

        # ============Train classifier=============

        clf=cv.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write(r'D:\MyPythonProgramming\Face detection attendance system\classifier.xml')
        cv.destroyAllWindows()
        messagebox.showinfo('Result','Training data set completed!')

if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()