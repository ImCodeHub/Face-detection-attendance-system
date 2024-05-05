from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk



class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")

        image = Image.open(r'D:\MyPythonProgramming\LoginFarm\nature3.jpg')
        image = image.resize((1920, 1080), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()