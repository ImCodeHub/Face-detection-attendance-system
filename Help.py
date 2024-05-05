from tkinter import *

from tokenize import String
from turtle import radians, title, width
from PIL import Image, ImageTk


class help:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management system")
        self.root.geometry("1920x1080+0+0")
        self.root.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')


        # =========background image==========
        image = Image.open(f'D:\MyPythonProgramming\Face detection attendance system\projectImage\Help2.jpg')
        image = image.resize((1550, 1080), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)

        background = Label(self.root, image=self.bg)
        background.place(x=0, y=0)
        # ======title=======
        Title = Label(background, text="Help Desk", font=(
            'arial', 50, 'bold'), fg="white", bg='#1b172b')
        Title.place(x=60, y=30)

        
        # ==========label=========
        
        DeveloperLabel = Label(
            background, text='narendrasharma720@yahoo.com', font=('arial', 40, 'bold'),bg='white')
        DeveloperLabel.place(x=500,y=400)
        

        

if __name__ == "__main__":
    root = Tk()
    app = help(root)
    root.mainloop()