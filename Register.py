from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from click import command
import mysql.connector



class RegisterNow:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")
        
        self.root.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')

        """background image"""
        image = Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\nature3.jpg')
        image = image.resize((1920, 1080), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)

        """left image"""
        image2 = Image.open(r'D:\MyPythonProgramming\Face detection attendance system\projectImage\FR1.jpg')
        image2 = image2.resize((300, 500), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(image2)
        leftimg = Label(self.root, image=self.bg1)
        leftimg.place(x=200, y=180, width=300, height=500)

        """"Variable"""""
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.mobileno = StringVar()
        self.emailid = StringVar()
        self.securityQ = StringVar()
        self.securityA = StringVar()
        self.password = StringVar()
        self.cpassword = StringVar()
        self.checbox = IntVar()

        """main frame"""
        frame = Frame(self.root, bg="#383836")
        frame.place(x=500, y=180, width=800, height=500)

        # Register label
        Register_lbl = Label(frame, text="REGISTER HERE", font=(
            'courier', 25, 'bold'), bg='#383836', fg='white')
        Register_lbl.place(x=15, y=15)
        # lable register entry
        fname = Label(frame, text='First name', font=(
            'courier', 20, 'bold'), bg='#383836', fg='white')
        fname.place(x=15, y=90)

        self.fname_entry = ttk.Entry(
            frame, text='First name', textvariable=self.firstname, font=('courier', 20))
        self.fname_entry.place(x=15, y=130)

        lname = Label(frame, text='Last name', font=(
            'courier', 20, 'bold'), bg='#383836', fg='white')
        lname.place(x=390, y=90)

        self.lname_entry = ttk.Entry(
            frame, text='Last name', textvariable=self.lastname, font=('courier', 20))
        self.lname_entry.place(x=390, y=130)

        """mobile no"""
        mobileno = Label(frame, text="Mobile number", font=(
            "courier", 20, 'bold'), fg='white', bg='#383836')
        mobileno.place(x=15, y=180)

        self.mobile_entry = ttk.Entry(
            frame, text='Mobile number', textvariable=self.mobileno, font=('courier', 20))
        self.mobile_entry.place(x=15, y=220)

        """Email"""

        email = Label(frame, text="Email ID", font=(
            "courier", 20, 'bold'), fg='white', bg='#383836')
        email.place(x=390, y=180)

        self.email_entry = ttk.Entry(
            frame, text='Email ID', textvariable=self.emailid, font=('courier', 20))
        self.email_entry.place(x=390, y=220)

        """Security"""

        SecurityQ = Label(frame, text="Security question", font=(
            "courier", 20, 'bold'), fg='white', bg='#383836')
        SecurityQ.place(x=15, y=270)

        self.SecurityQ_entry = ttk.Combobox(
            frame, text='Security question', textvariable=self.securityQ, font=('courier', 18), state='readonly')
        self.SecurityQ_entry['values'] = (
            'Select', 'Your father', 'your mother', 'your best friend')
        self.SecurityQ_entry.place(x=15, y=310)
        # it will show index number in combobox
        self.SecurityQ_entry.current(0)

        SecurityA = Label(frame, text="Security Answer", font=(
            "courier", 20, 'bold'), fg='white', bg='#383836')
        SecurityA.place(x=390, y=270)

        self.SecurityA_entry = ttk.Entry(
            frame, text='Security Answer', font=('courier', 20))
        self.SecurityA_entry.place(x=390, y=310)

        """password"""

        Password = Label(frame, text="Password", font=(
            "courier", 20, 'bold'), fg='white', bg='#383836')
        Password.place(x=15, y=360)

        self.Password_entry = ttk.Entry(
            frame, text='Password', textvariable=self.password, font=('courier', 20))
        self.Password_entry.place(x=15, y=400)

        PasswordC = Label(frame, text="Password Confirmation", font=(
            "courier", 20, 'bold'), fg='white', bg='#383836')
        PasswordC.place(x=390, y=360)

        self.PasswordC_entry = ttk.Entry(
            frame, text='Password Confirmation', textvariable=self.cpassword, font=('courier', 20))
        self.PasswordC_entry.place(x=390, y=400)

        self.checkBox = Checkbutton(frame, text='I Agreed all the T&C', variable=self.checbox, font=(
            'courier', 15, 'bold', 'italic'), onvalue=1, offvalue=1, activebackground="#636260", activeforeground="white")
        self.checkBox.place(x=15, y=440)

        """Button"""
        RButtons = Button(frame, text="Register Now", command=self.Registerbtn, font=("courier", 15, "bold"), border=3,
                          fg="white", bg="#383836", relief=RIDGE, activebackground="#636260", activeforeground="white")
        RButtons.place(x=390, y=440)

        LButtons = Button(frame, text="Login Now",command=self.returnLogin, font=("courier", 15, "bold"), border=3,
                          fg="white", bg="#a83c32", relief=RIDGE, activebackground="#636260", activeforeground="white")
        LButtons.place(x=590, y=440)

    def Registerbtn(self):
        if self.firstname.get() == '' or self.emailid.get() == '' or self.securityQ.get() == 'select' or self.password.get() == '' or self.cpassword.get() == '':
            messagebox.showerror("Error", 'All fields are required')
        elif self.password.get() != self.cpassword.get():
            messagebox.showerror(
                'Password Error', 'Password and confirm password must be same')
        elif self.checbox.get() == 0:
            messagebox.showerror('Error', 'Please agree Terms and Condition')
        else:
            # messagebox.showerror('Error',self.SecurityA_entry.get())
            conn = mysql.connector.connect(
                user='root', password='password', host='localhost', database='testdb')
            MyCursor = conn.cursor()
            query = ("select * from user where email=%s")
            value = (self.emailid.get(),)
            MyCursor.execute(query, value)
            record = MyCursor.fetchone()
            if record != None:
                messagebox.showerror(
                    'Error', 'User already exist,try another email or mobile number.')
            else:
                MyCursor.execute("insert into USER(firstName, lastName, mobileno, email, SecurityQ, SecurityA, password) values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.fname_entry.get(),
                    self.lastname.get(),
                    self.mobileno.get(),
                    self.emailid.get(),
                    self.securityQ.get(),
                    self.SecurityA_entry.get(),
                    self.password.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('success', 'Registered successfully')

    def returnLogin(self):
        self.root.destroy()

    # def LoginWindow(self):
    #     self.NewWindow=Toplevel(self.root)
    #     self.app=LoginWindow(self.NewWindow) 

if __name__ == "__main__":
    root = Tk()
    app = RegisterNow(root)
    root.mainloop()
