from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tokenize import String
from turtle import radians, title, width
from PIL import Image, ImageTk
from numpy import imag, record
import mysql.connector
import cv2 as cv


class developer:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management system")
        self.root.geometry("1920x1080+0+0")
        self.root.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')


        # =========background image==========
        image = Image.open(f'D:\MyPythonProgramming\Face detection attendance system\projectImage\FR4.jpg')
        
        self.bg = ImageTk.PhotoImage(image)

        background = Label(self.root, image=self.bg)
        background.place(x=0, y=0)
        # ======title=======
        Title = Label(background, text="Devloper", font=(
            'arial', 50, 'bold'), fg="white", bg='#1b172b')
        Title.place(x=100, y=30)

        # =======frame==========
        mainFrame=Frame(background,bd=2,bg='white')
        mainFrame.place(x=1000,y=150,width=400,height=600)

        # ==========label=========
        DeveloperLabel = Label(
            mainFrame, text='Hi, My name is Narendra', font=('arial', 16, 'bold'),bg='white')
        DeveloperLabel.place(x=10,y=20)

        DeveloperLabel = Label(
            mainFrame, text='And i am full stack Developer', font=('arial', 16, 'bold'),bg='white')
        DeveloperLabel.place(x=10,y=50)

        DeveloperLabel = Label(
            mainFrame, text='my contact number is : 7987179297', font=('arial', 16, 'bold'),bg='white')
        DeveloperLabel.place(x=10,y=80)
        # ===========image=======

        image2 = Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\Developerman.jpg')
        image2 = image2.resize((400, 300), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(image2)
        leftimg = Label(mainFrame, image=self.bg1)
        leftimg.place(x=0, y=200, width=400, height=450)

if __name__ == "__main__":
    root = Tk()
    app = developer(root)
    root.mainloop()