from operator import le
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tokenize import String
from turtle import radians, title, width
from PIL import Image, ImageTk
from numpy import imag, record
import mysql.connector
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management system")
        self.root.geometry("1920x1080+0+0")
        self.root.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')


        # ==========Variable===========
        self.AttendanceidV=StringVar()
        self.RollNoV=StringVar()
        self.NameV=StringVar()
        self.DepartmentV=StringVar()
        self.TimeV=StringVar()
        self.DateV=StringVar()
        self.AttendanceStatusV=StringVar()

        # =========background image==========
        image = Image.open(
            r'D:\MyPythonProgramming\Face detection attendance system\projectImage\StdBackground.jpg')
        image = image.resize((2220, 800), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)

        background = Label(self.root, image=self.bg)
        background.place(x=0, y=0)

        # ===========title label===========
        Title = Label(background, text="Student Management System Gyanoday college Neemuch (m.p.)", font=(
            'arial', 30, 'bold'), fg="white", bg='#14151c')
        Title.place(x=20, y=30)

        # ==========Main Frame===========
        MainFrame = Frame(background, bd=3)
        MainFrame.place(x=60, y=150, width=1410, height=600)

        # ========== left label Frame===========
        LeftFrame = LabelFrame(MainFrame, bd=4, relief=RIDGE,
                               text='Student Attendance Details', font=('arial', 15, 'bold'))
        LeftFrame.place(x=10, y=10, width=675, height=570)

        course = LabelFrame(LeftFrame, bd=4, relief=RIDGE,
                            text='Course Details', font=('courier', 15, 'bold'))
        course.place(x=10, y=100, width=645, height=100)

        leftImg = Image.open(
            r'D:\MyPythonProgramming\Face detection attendance system\projectImage\Attendance1.jpg')
        leftImg = leftImg.resize((675, 200), Image.ANTIALIAS)
        self.leftFrameImg = ImageTk.PhotoImage(leftImg)

        leftImgLabel = Label(LeftFrame, image=self.leftFrameImg)
        leftImgLabel.place(x=10, y=10, width=645, height=200)

        LeftLabelFrame = LabelFrame(
            LeftFrame, bd=3, relief=RIDGE, text='Attendance ID', font=('arial', 15, 'bold'))
        LeftLabelFrame.place(x=10, y=230, width=649, height=300)

        # ===========Lables Entery================
        # Attendance ID

        AttendanceidLabel = Label(
            LeftLabelFrame, text='Attendance ID:', font=('arial', 12, 'bold'))
        AttendanceidLabel.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        AttendanceidEntery = ttk.Entry(LeftLabelFrame, font=(
            'arial', 12),textvariable=self.AttendanceidV)
        AttendanceidEntery.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Studen roll

        RollNoLabel = Label(
            LeftLabelFrame, text='Roll No:', font=('arial', 12, 'bold'))
        RollNoLabel.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        RollNoEntery = ttk.Entry(LeftLabelFrame, font=(
            'arial', 12),textvariable=self.RollNoV)
        RollNoEntery.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Name

        NameLabel = Label(
            LeftLabelFrame, text='Name :', font=('arial', 12, 'bold'))
        NameLabel.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        NameEntery = ttk.Entry(LeftLabelFrame, font=(
            'arial', 12),textvariable=self.NameV)
        NameEntery.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Department
        DepartmentLabel = Label(
            LeftLabelFrame, text='Department :', font=('arial', 12, 'bold'))
        DepartmentLabel.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        DepartmentEntery = ttk.Entry(LeftLabelFrame, font=(
            'arial', 12),textvariable=self.DepartmentV)
        DepartmentEntery.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Time

        TimeLabel = Label(
            LeftLabelFrame, text='Time :', font=('arial', 12, 'bold'))
        TimeLabel.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        TimeEntery = ttk.Entry(LeftLabelFrame, font=(
            'arial', 12),textvariable=self.TimeV)
        TimeEntery.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Date
        DateLabel = Label(
            LeftLabelFrame, text='Date :', font=('arial', 12, 'bold'))
        DateLabel.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        DateEntery = ttk.Entry(LeftLabelFrame, font=(
            'arial', 12),textvariable=self.DateV)
        DateEntery.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Attendamce Status
        AttendanceStatusLabel = Label(
            LeftLabelFrame, text='Status :', font=('arial', 12, 'bold'))
        AttendanceStatusLabel.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        AttendanceStatusCombo = ttk.Combobox(
            LeftLabelFrame, font=('arial', 12, 'bold'), state='readonly', width=18,textvariable=self.AttendanceStatusV)
        AttendanceStatusCombo['values'] = ('Present', 'Absent')
        AttendanceStatusCombo.current(0)
        AttendanceStatusCombo.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # =============Buttons============
        buttonframe = Frame(LeftLabelFrame, bd=1, relief=SOLID)
        buttonframe.place(x=10, y=200, width=621, height=34)

        impotbtn = Button(buttonframe, text='Import csv',command=self.importCsv,width=15, font=('arial', 12, 'bold'), bg='#32a885')
        impotbtn.grid(row=0, column=0)

        exportbtn = Button(buttonframe, text='Export csv', width=14,command=self.exportCsv,
                           font=('arial', 12, 'bold'), bg='#32a885')
        exportbtn.grid(row=0, column=1)

        updatebtn = Button(buttonframe, text='Update', width=15, font=(
            'arial', 12, 'bold'), bg='#32a885')
        updatebtn.grid(row=0, column=2)

        Resetbtn = Button(buttonframe, text='Reset', width=14,
                          font=('arial', 12, 'bold'), bg='#32a885',command=self.resetData)
        Resetbtn.grid(row=0, column=3)

        # ===============Right side frame==============
        RightFrame = LabelFrame(
            MainFrame, bd=5, relief=RIDGE, text='Attendance details', font=('courier', 15, 'bold'))
        RightFrame.place(x=690, y=10, width=708, height=570)

        TableFrame = LabelFrame(
            RightFrame, bd=4, relief=RIDGE, font=('courier', 15, 'bold'))
        TableFrame.place(x=10, y=10, width=680, height=517)

        # =========Scroller======
        ScrollX = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        ScrollY = ttk.Scrollbar(TableFrame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(TableFrame, column=(
            'id', 'RollNo', 'Name', 'Department', 'Time', 'Date', 'Attendance'), xscrollcommand=ScrollX.set, yscrollcommand=ScrollY.set)

        ScrollX.pack(side=BOTTOM, fill=X)
        ScrollY.pack(side=RIGHT, fill=Y)

        ScrollX.config(command=self.AttendanceReportTable.xview)
        ScrollY.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('id',text='Attendance ID')
        self.AttendanceReportTable.heading('RollNo',text='Roll No')
        self.AttendanceReportTable.heading('Name',text='Name')
        self.AttendanceReportTable.heading('Department',text='Department')
        self.AttendanceReportTable.heading('Time',text='Time')
        self.AttendanceReportTable.heading('Date',text='Date')
        self.AttendanceReportTable.heading('Attendance',text='Attendance')

        self.AttendanceReportTable['show']='headings'  # to remove space between headings column.
        self.AttendanceReportTable.column('id',width=100)
        self.AttendanceReportTable.column('RollNo',width=100)
        self.AttendanceReportTable.column('Name',width=100)
        self.AttendanceReportTable.column('Department',width=100)
        self.AttendanceReportTable.column('Time',width=100)
        self.AttendanceReportTable.column('Date',width=100)
        self.AttendanceReportTable.column('Attendance',width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind('<ButtonRelease>',self.getCursor)

        # ================Fetch DATA================
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert('',END,values=i)

    #=========Import csv==========        

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(title='open CSV',filetype=(('CSV file','*.csv'),('All file','*.*')),parent=self.root)
        with open(fln) as myfile:   
            csvread=csv.reader(myfile,delimiter=',')
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    # =========Export CSV===========
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror('No Data','No Data found to Export',parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(title='open CSV',filetype=(('CSV file','*.csv'),('All file','*.*')),parent=self.root)
            with open(fln,mode='w',newline='') as myfile:
                expWrite=csv.writer(myfile,delimiter=',')
                for i in mydata:
                    expWrite.writerow(i)
                messagebox.showinfo('Data Export','Your Data exported to '+os.path.basename(fln)+' Successfully')     
        except Exception as es:
            messagebox.showerror('Error',f'Due to : {str(es)}',parent=self.root)

    def getCursor(self,event=''):
        cursorRow=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursorRow)
        rows=content['values']
        self.AttendanceidV.set(rows[0])
        self.RollNoV.set(rows[1])
        self.NameV.set(rows[2])
        self.DepartmentV.set(rows[3])
        self.TimeV.set(rows[4])
        self.DateV.set(rows[5])
        self.AttendanceStatusV.set(rows[6])

    def resetData(self):
        self.AttendanceidV.set("")
        self.RollNoV.set("")
        self.NameV.set("")
        self.DepartmentV.set("")
        self.TimeV.set("")
        self.DateV.set("")
        self.AttendanceStatusV.set("")


if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()
