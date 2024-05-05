from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from Register import RegisterNow
from FaceRecognition import FaceRecognition

conn = mysql.connector.connect(user='root', password='password', host='localhost', database='testdb')
def main():
    win = Tk()
    # win.iconbitmap('faceicon.ico')
    app = LoginWindow(win)
    win.mainloop()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry("1920x1080+0+0")
        self.root.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')
        
        
        self.bg = ImageTk.PhotoImage(
            file=r'D:\MyPythonProgramming\Face detection attendance system\projectImage\1170024.jpg')
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        clgName=Label(self.root,text='Face Recognition Attendance System Gyanoday college Neemuch(m.p.)',font=('arial',30,'bold'))
        clgName.place(x=100,y=90)

        frame = Frame(self.root, bg="#383836")
        frame.place(x=610, y=170, width=340, height=450)

        GetStart = Label(frame, text="Get Started", font=(
            "courier", 20, "bold"), fg="white", bg="#383836")
        GetStart.place(x=80, y=60)

        #==========variable=============
        self.userNameV=StringVar()
        self.passwordV=StringVar()
        

        # label
        # username
        username = lbl = Label(frame, text="user name", font=(
            "courier", 15), fg="white", bg="#383836")
        username.place(x=60, y=100)

        self.txtuser = ttk.Entry(frame, font=("courier", 15),textvariable=self.userNameV)
        self.txtuser.place(x=60, y=130)

        # password
        Password = lbl2 = Label(frame, text="Password", font=(
            "courier", 15), fg="white", bg="#383836")
        Password.place(x=60, y=190)

        self.txtpass = ttk.Entry(frame, show="*", font=("courier", 15),textvariable=self.passwordV)
        self.txtpass.place(x=60, y=220)

        # login buttion
        LoginButton = Button(frame, command=self.loginbtn, text="Login", font=("courier", 15, "bold"), border=3,
                             fg="white", bg="#383836", relief=RIDGE, activebackground="#636260", activeforeground="white")
        LoginButton.place(x=135, y=280)

        # register
        Register = Button(frame, text='Register Now',command=self.RegisterWindow, font=('courier', 10), bd=0,
                          fg='white', bg='#383836', activebackground='#383836', activeforeground="white")
        Register.place(x=60, y=350)

        ForgotPassword = Button(frame, text='Forgot password', font=(
            'courier', 10),command=self.forgotPassword, bd=0, fg='white', bg='#383836', activebackground='#383836', activeforeground="white")
        ForgotPassword.place(x=60, y=380)
 
    def RegisterWindow(self):
        self.NewWindow=Toplevel(self.root)
        self.app=RegisterNow(self.NewWindow)    

    def loginbtn(self):
        if self.userNameV.get()=="" or self.passwordV=="":
            messagebox.showerror('Error','All field required!')
        else:
            conn = mysql.connector.connect(user='root', password='password', host='localhost', database='testdb')
            Mycursor = conn.cursor()

            # query = ('select * from User where email = %s and password=%s')
            # data = (userName, password)
            # cursor.execute(query, data)  # select query for user # this is also similar as mentioned code below

            Mycursor.execute('select * from User where email = %s and password=%s',(self.userNameV.get(),self.passwordV.get()))
            record = Mycursor.fetchone()
        if record ==None:
            messagebox.showerror("Error", "Invalid username and ID")
        else:
            openMain=messagebox.askyesno("Yes or No", "Are you wants to login ?")
            if openMain>0:
                self.NewWindow=Toplevel(self.root)
                self.app=FaceRecognition(self.NewWindow)
            else:
                if not openMain:
                    return
        conn.commit()
        # self.clear()
        conn.close()
    
    # =========reset password==========
    def resetPassword(self):
        if self.SecurityQV.get()=='Select':
            messagebox.showerror('Error','Select Security question.')
        elif self.SecurityAV.get()=='':
            messagebox.showerror('Error','Please, Enter the correct Answer')
        elif self.newpassV.get()=='':
            messagebox.showerror('Error','Please, Enter the New Password')
        else:
            conn = mysql.connector.connect(user='root', password='password', host='localhost', database='testdb')
            Mycursor=conn.cursor()
            query=('select* from User where email=%s and SecurityQ=%s and SecurityA=%s')
            value=(self.userNameV.get(),self.SecurityQV.get(),self.SecurityAV.get())

            Mycursor.execute(query,value)
            record=Mycursor.fetchone()
            if record==None:
                messagebox.showerror('Error','Please Enter correct Answer',parent=self.root2)
            else:
                query=('update User set password=%s where email=%s')
                value=(self.newpassV.get(),self.userNameV.get())
                Mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo('Info','Your password has been Reset, Please login with new password.',parent=self.root2)
                self.root2.destroy()




    # ===========forgot password window==============
    def forgotPassword(self):
        if self.userNameV.get()=='':
            messagebox.showerror('Error','Please Enter the E-main id to Rest password.')
        else:
            conn = mysql.connector.connect(user='root', password='password', host='localhost', database='testdb')
            Mycursor=conn.cursor()
            Mycursor.execute('select * from User where email=%s',(self.userNameV.get(),))
            record=Mycursor.fetchone()
            # print(record)
            if record==None:
                messagebox.showerror('Error','Please Enter the valid Username.')
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title('Forgot Password')
                self.root2.geometry('340x450+610+170')
                self.root2.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')
                # ======frame=======
                frame = Frame(self.root2, bg="#a83c32")
                frame.place(x=0, y=0, width=340, height=450)

                # ========variable=========
                self.SecurityQV=StringVar()
                self.SecurityAV=StringVar()
                self.newpassV=StringVar()
                
                # ========labels===========
                l = Label(frame, text="Forgot Password",font=('arial',20,'bold'), fg="white", bg='#a83c32')
                l.place(x=0,y=10, relwidth=1)
                 
                SecurityQ = Label(frame, text="Security question", font=(
                    "courier", 15,'bold'), fg='white', bg='#a83c32')
                SecurityQ.place(x=25, y=90)

                self.SecurityQ_entry = ttk.Combobox(
                    frame, text='Security question',textvariable=self.SecurityQV
                    , font=('courier', 12,'bold'), state='readonly')
                self.SecurityQ_entry['values'] = (
                    'Select', 'Your father', 'your mother', 'your best friend')
                self.SecurityQ_entry.place(x=42, y=120,width=249,height=30)
                # it will show index number in combobox
                self.SecurityQ_entry.current(0)

                SecurityA = Label(frame, text="Security Answer", font=(
                    "courier", 15, 'bold'), fg='white', bg='#a83c32')
                SecurityA.place(x=25, y=170)

                self.SecurityA_entry = ttk.Entry(
                    frame, text='Security Answer',textvariable=self.SecurityAV, font=('courier'))
                self.SecurityA_entry.place(x=42, y=200,width=249,height=30)

                resetPass = Label(frame, text="New password", font=(
                    "courier", 15, 'bold'), fg='white', bg='#a83c32')
                resetPass.place(x=25, y=250)

                self.resetPassEntry = ttk.Entry(
                    frame, text='Security Answer',textvariable=self.newpassV, font=('courier'))
                self.resetPassEntry.place(x=42, y=280,width=249,height=30)

                resetButton = Button(frame, text="Reset password",command=self.resetPassword, font=("courier", 15, "bold"), border=3,
                             fg="white", bg="#383836", relief=RIDGE, activebackground="#636260", activeforeground="white")
                resetButton.place(x=80, y=350)






if __name__ == "__main__":
    main()
