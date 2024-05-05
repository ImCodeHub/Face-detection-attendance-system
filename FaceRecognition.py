from cgitb import text
from time import strftime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk
from numpy import imag
from Students import Students
import os
from Train import Train
from FaceIdentification import faceRecognition_System
from Attendance import Attendance
from Developer import developer
from Help import help
from datetime import datetime
from time import strftime

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition")
        self.root.geometry("1920x1080+0+0")
        self.root.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')

        # =========background image==========
        image = Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\FR4.jpg')
        image = image.resize((2009,1299), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)
        background=Label(self.root,image=self.bg)
        background.place(x=0,y=0)
        # ===========title label===========
        Title=Label(background,text="Face Recognistion Attendance system Gyanodya college Neemuch (m.p.)",font=('arial',20,'bold'),fg="white",bg='#14092b')
        Title.place(x=20,y=30)

        #  ==========time===========
        def times():
            string= strftime("%d-%m-%Y    %H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,times)
        lbl=Label(background,font=('arial',20,'bold'),fg="white",bg='#14092b')
        lbl.place(x=20,y=80)
        times()

        # =============student button =========

        img1=Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\studentImage.jpg')
        img1=img1.resize((220,220),Image.ANTIALIAS)
        self.stdimg=ImageTk.PhotoImage(img1)

        b1=Button(background,image=self.stdimg,command=self.Studentsbtn,cursor='hand2')
        b1.place(x=200,y=150,width='220',height='220')
        
        b1btn=Button(background,text='Student Details',command=self.Studentsbtn,cursor='hand2',font='arial',bg='#0a3269',fg='white')
        b1btn.place(x=200,y=368,width='220',height='40')

        # ============Face Recognition=========

        img2=Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\Rcgn.jpg')
        img2=img2.resize((220,220),Image.ANTIALIAS)
        self.face=ImageTk.PhotoImage(img2)

        b1=Button(background,image=self.face,command=self.faceRecognition_System,cursor='hand2')
        b1.place(x=500,y=150,width='220',height='220')
        
        b1btn2=Button(background,text='Face Recognition',command=self.faceRecognition_System,cursor='hand2',font='arial',bg='#0a3269',fg='white')
        b1btn2.place(x=500,y=368,width='220',height='40')

        # ==============Attendance face button=============

        img3=Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\Attendance.jpg')
        img3=img3.resize((220,220),Image.ANTIALIAS)
        self.faceAttendance=ImageTk.PhotoImage(img3)

        b1=Button(background,image=self.faceAttendance,command=self.Attendance,cursor='hand2')
        b1.place(x=800,y=150,width='220',height='220')
        
        b1btn2=Button(background,text='Attendance',command=self.Attendance,cursor='hand2',font='arial',bg='#0a3269',fg='white')
        b1btn2.place(x=800,y=368,width='220',height='40')

        # ===============Help button===============

        img4=Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\help1.jpg')
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.Helpbtn=ImageTk.PhotoImage(img4)

        b1=Button(background,image=self.Helpbtn,cursor='hand2',command=self.help)
        b1.place(x=1100,y=150,width='220',height='220')
        
        b1btn2=Button(background,text='Help',cursor='hand2',font='arial',bg='#0a3269',fg='white',command=self.help)
        b1btn2.place(x=1100,y=368,width='220',height='40')

        # ===============Train Data button===============

        img5=Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\TrainData.jpg')
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.TrainDatabtn=ImageTk.PhotoImage(img5)

        b1=Button(background,image=self.TrainDatabtn,command=self.Train,cursor='hand2')
        b1.place(x=200,y=450,width='220',height='220')
        
        b1btn2=Button(background,text='Train DATA',command=self.Train,cursor='hand2',font='arial',bg='#0a3269',fg='white')
        b1btn2.place(x=200,y=668,width='220',height='40')

         # ===============Photos button===============

        img6=Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\photo.jpg')
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.Photobtn=ImageTk.PhotoImage(img6)

        b1=Button(background,image=self.Photobtn,cursor='hand2',command=self.open_img)
        b1.place(x=500,y=450,width='220',height='220')
        
        b1btn2=Button(background,text='Photos',cursor='hand2',command=self.open_img,font='arial',bg='#0a3269',fg='white')
        b1btn2.place(x=500,y=668,width='220',height='40')

        # ===============Developer button===============

        img7=Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\developer.jpg')
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.Developerbtn=ImageTk.PhotoImage(img7)

        b1=Button(background,image=self.Developerbtn,cursor='hand2',command=self.developer)
        b1.place(x=800,y=450,width='220',height='220')
        
        b1btn2=Button(background,text='Developer',cursor='hand2',font='arial',bg='#0a3269',fg='white',command=self.developer)
        b1btn2.place(x=800,y=668,width='220',height='40')

         # ===============Exit button===============

        img8=Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\exit.jpg')
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.Exitbtn=ImageTk.PhotoImage(img8)

        b1=Button(background,image=self.Exitbtn,cursor='hand2',command=self.iExit)
        b1.place(x=1100,y=450,width='220',height='220')
        
        b1btn2=Button(background,text='Exit',cursor='hand2',font='arial',bg='#0a3269',fg='white',command=self.iExit)
        b1btn2.place(x=1100,y=668,width='220',height='40')

    def open_img(self):
        os.startfile(r'D:\MyPythonProgramming\Face detection attendance system\photosample') 

    def iExit(self):
        self.iExit=messagebox.askyesno('Face Recognition','Are you sure you wants to Exit',parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return



        # =========Function button========
    def Studentsbtn(self):
        self.NewWindow=Toplevel(self.root)
        self.app=Students(self.NewWindow) 

    def Train(self):
        self.NewWindow=Toplevel(self.root)
        self.app=Train(self.NewWindow) 

    def faceRecognition_System(self):
        self.NewWindow=Toplevel(self.root)
        self.app=faceRecognition_System(self.NewWindow) 

    def Attendance(self):
        self.NewWindow=Toplevel(self.root)
        self.app=Attendance(self.NewWindow)

    def developer(self):
        self.NewWindow=Toplevel(self.root)
        self.app=developer(self.NewWindow) 

    def help(self):
        self.NewWindow=Toplevel(self.root)
        self.app=help(self.NewWindow) 
        




if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    root.mainloop()
