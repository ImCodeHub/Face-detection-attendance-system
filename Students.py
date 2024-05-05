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


class Students:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management system")
        self.root.geometry("1920x1080+0+0")
        self.root.iconbitmap(r'D:\MyPythonProgramming\Face detection attendance system\faceid3.ico')


        # =========background image==========
        image = Image.open(f'D:\MyPythonProgramming\Face detection attendance system\projectImage\StdBackground.jpg')
        image = image.resize((2220, 800), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)

        background = Label(self.root, image=self.bg)
        background.place(x=0, y=0)

        # ===========title label===========
        Title = Label(background, text="Student Management System Gyanoday college Neemuch", font=(
            'arial', 30, 'bold'), fg="white", bg='#14151c')
        Title.place(x=20, y=30)

        # ==========Frame===========
        MainFrame = Frame(background, bd=3)
        MainFrame.place(x=60, y=150, width=1410, height=600)

        # ========== left label Frame===========
        LeftFrame = LabelFrame(MainFrame, bd=4, relief=RIDGE,
                               text='Student Details', font=('arial', 15, 'bold'))
        LeftFrame.place(x=10, y=10, width=675, height=570)

        course = LabelFrame(LeftFrame, bd=1, relief=SOLID,
                            text='Course Details', font=('courier', 15, 'bold'))
        course.place(x=10, y=10, width=645, height=100)

        # ===========Text Variable============
        self.departmentComboV = StringVar()
        self.CourseComboV = StringVar()
        self.YearComboV = StringVar()
        self.SemesterComboV = StringVar()
        self.StudentidEnteryV = StringVar()
        self.StudentNameEntryV = StringVar()
        self.ClassEnteryV = StringVar()
        self.RollnoEntryV = StringVar()
        self.GenderEnteryV = StringVar()
        self.DOBEntryV = StringVar()
        self.EmailEntryV = StringVar()
        self.MobilenoEntryV = StringVar()
        self.AddressEnteryV = StringVar()
        self.TeacherEntryV = StringVar()

        departmentLabel = Label(course, text='Department', font=('arial', 12))
        departmentLabel.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        departmentCombo = ttk.Combobox(course, font=(
            'arial', 12), textvariable=self.departmentComboV, state='readonly')
        departmentCombo['values'] = (
            "Select Department", 'Computer', 'IT', 'Civil', 'Mechanical')
        departmentCombo.current(0)
        departmentCombo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # course
        CourseLabel = Label(course, text='Course', font=('arial', 12))
        CourseLabel.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        CourseCombo = ttk.Combobox(course, font=(
            'arial', 12), textvariable=self.CourseComboV, state='readonly')
        CourseCombo['values'] = (
            "Select Department", 'BCA', 'B.Sc', 'MCA', 'MBA', 'M.Sc')
        CourseCombo.current(0)
        CourseCombo.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Year
        YearLabel = Label(course, text='Year', font=('arial', 12))
        YearLabel.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        YearCombo = ttk.Combobox(course, font=(
            'arial', 12), textvariable=self.YearComboV, state='readonly')
        YearCombo['values'] = ("Select Year", '2022-23',
                               '2023-24', '2024-25', '2025-26')
        YearCombo.current(0)
        YearCombo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Semester

        SemesterLabel = Label(course, text='Semester', font=('arial', 12))
        SemesterLabel.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        SemesterCombo = ttk.Combobox(course, font=(
            'arial', 12), textvariable=self.SemesterComboV, state='readonly')
        SemesterCombo['values'] = (
            "Select Semester", '1st sem', '2nd sem', '3rd sem', '4th sem', '5th sem', '6th sem')
        SemesterCombo.current(0)
        SemesterCombo.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # ========class student information========

        ClassStudent = LabelFrame(LeftFrame, bd=1, relief=SOLID,
                                  text='Student class Details', font=('courier', 15, 'bold'))
        ClassStudent.place(x=10, y=115, width=645, height=350)

        # studen id
        StudentidLabel = Label(
            ClassStudent, text='Student ID:', font=('arial', 12))
        StudentidLabel.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        StudentidEntery = ttk.Entry(ClassStudent, font=(
            'arial', 12), textvariable=self.StudentidEnteryV)
        StudentidEntery.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        # Student name
        StudentNameLabel = Label(
            ClassStudent, text='Student Name:', font=('arial', 12))
        StudentNameLabel.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        StudentNameEntry = ttk.Entry(ClassStudent, font=(
            'arial', 12), textvariable=self.StudentNameEntryV)
        StudentNameEntry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # class Devision
        ClassLabel = Label(
            ClassStudent, text='Class Devision:', font=('arial', 12))
        ClassLabel.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        # ClassEntery=ttk.Entry(ClassStudent,font=('arial',12),textvariable=self.ClassEnteryV)
        # ClassEntery.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        devisionCombo = ttk.Combobox(ClassStudent, font=(
            'arial', 12), textvariable=self.ClassEnteryV, state='readonly', width=18)
        devisionCombo['values'] = ("Select Devision", 'A', 'B', 'C')
        devisionCombo.current(0)
        devisionCombo.grid(row=1, column=1, padx=5, pady=6, sticky=W)

        # Roll no
        RollnoLabel = Label(ClassStudent, text='Roll No:', font=('arial', 12))
        RollnoLabel.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        RollnoEntry = ttk.Entry(ClassStudent, font=(
            'arial', 12), textvariable=self.RollnoEntryV)
        RollnoEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender
        GenderLabel = Label(ClassStudent, text='Gender:', font=('arial', 12))
        GenderLabel.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        # GenderEntery=ttk.Entry(ClassStudent,font=('arial',12),textvariable=self.GenderEnteryV)
        # GenderEntery.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        genderCombo = ttk.Combobox(ClassStudent, font=(
            'arial', 12), textvariable=self.GenderEnteryV, state='readonly', width=18)
        genderCombo['values'] = ("Select Gender", 'Male', 'Female')
        genderCombo.current(0)
        genderCombo.grid(row=2, column=1, padx=5, pady=6, sticky=W)

        # DOB
        DOBLabel = Label(ClassStudent, text='DOB:', font=('arial', 12))
        DOBLabel.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        DOBEntry = ttk.Entry(ClassStudent, font=(
            'arial', 12), textvariable=self.DOBEntryV)
        DOBEntry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Email
        EmailLabel = Label(ClassStudent, text='Email ID:', font=('arial', 12))
        EmailLabel.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        EmailEntery = ttk.Entry(ClassStudent, font=(
            'arial', 12), textvariable=self.EmailEntryV)
        EmailEntery.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Mobileno
        MobilenoLabel = Label(
            ClassStudent, text='Mobile No:', font=('arial', 12))
        MobilenoLabel.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        MobilenoEntry = ttk.Entry(ClassStudent, font=(
            'arial', 12), textvariable=self.MobilenoEntryV)
        MobilenoEntry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address
        AddressLabel = Label(ClassStudent, text='Address:', font=('arial', 12))
        AddressLabel.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        AddressEntery = ttk.Entry(ClassStudent, font=(
            'arial', 12), textvariable=self.AddressEnteryV)
        AddressEntery.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Teacher
        TeacherLabel = Label(ClassStudent, text='Teacher:', font=('arial', 12))
        TeacherLabel.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        TeacherEntry = ttk.Entry(ClassStudent, font=(
            'arial', 12), textvariable=self.TeacherEntryV)
        TeacherEntry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # =======Radio button=========
        self.radio = StringVar()
        Radiobtn1 = ttk.Radiobutton(
            ClassStudent, text='Take photo sample', variable=self.radio, value='Yes')
        Radiobtn1.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        Radiobtn2 = ttk.Radiobutton(
            ClassStudent, text='No photo sample', variable=self.radio, value='No')
        Radiobtn2.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        # =========Button frame==========

        buttonframe = Frame(ClassStudent, bd=1, relief=SOLID)
        buttonframe.place(x=10, y=210, width=621, height=34)

        Savebtn = Button(buttonframe, text='Save', command=self.AddData,
                         width=15, font=('arial', 12, 'bold'), bg='Lightblue')
        Savebtn.grid(row=0, column=0)

        Updatebtn = Button(buttonframe, text='Update', width=14,command=self.updateData,
                           font=('arial', 12, 'bold'), bg='Lightblue')
        Updatebtn.grid(row=0, column=1)

        Deletebtn = Button(buttonframe, text='Delete',command=self.deleteData, width=15, font=(
            'arial', 12, 'bold'), bg='red', fg='white')
        Deletebtn.grid(row=0, column=2)

        Resetbtn = Button(buttonframe, text='Reset', width=14,command=self.resetData,
                          font=('arial', 12, 'bold'), bg='Lightblue')
        Resetbtn.grid(row=0, column=3)

        buttonframe1 = Frame(ClassStudent, bd=1, relief=SOLID)
        buttonframe1.place(x=10, y=246, width=621, height=34)

        TakePhotobtn = Button(buttonframe1, text='Take Photo Sample',command=self.generateDataset, width=30, font=(
            'arial', 12, 'bold'), bg='Lightblue')
        TakePhotobtn.grid(row=0, column=0)

        Updatebtn = Button(buttonframe1, text='Update Photo Sample', width=30, font=(
            'arial', 12, 'bold'), bg='Lightblue')
        Updatebtn.grid(row=0, column=1)

        # ========== right label Frame===========
        RightFrame = LabelFrame(
            MainFrame, bd=5, relief=RIDGE, text='Student details', font=('courier', 15, 'bold'))
        RightFrame.place(x=690, y=10, width=708, height=570)

        # ============Search system============
        SearchFrame = LabelFrame(
            RightFrame, bd=1, relief=SOLID, text='Search system', font=('courier', 15, 'bold'))
        SearchFrame.place(x=10, y=10, width=680, height=80)

        SearchLabel = Label(SearchFrame, text='Search by:', font=(
            'arial', 12, 'bold'), bg='red', fg='white')
        SearchLabel.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        self.searchV=StringVar()  #variable

        SearchCombo = ttk.Combobox(SearchFrame, width=15, textvariable=self.searchV, font=(
            'arial', 12, 'bold'), state='readonly')
        SearchCombo['values'] = ('Select', 'Roll No', 'Mobile No')
        SearchCombo.current(0)
        SearchCombo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.searchEntryV=StringVar()   #variable

        SearchEntery = ttk.Entry(SearchFrame, width=15, textvariable=self.searchEntryV, font=('arial', 12))
        SearchEntery.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        Search1btn = Button(SearchFrame, text='Search',command=self.search, width=10, font=(
            'arial', 12, 'bold'), bg='Lightgreen')
        Search1btn.grid(row=0, column=3, padx=5)

        SearchAllbtn = Button(SearchFrame, text='Search All',command=self.FetchData, width=10, font=(
            'arial', 12, 'bold'), bg='Lightgreen')
        SearchAllbtn.grid(row=0, column=4, padx=5)

        # ========Table Frame=======
        TableFrame = LabelFrame(
            RightFrame, bd=1, relief=SOLID, font=('courier', 15, 'bold'))
        TableFrame.place(x=10, y=100, width=680, height=400)

        ScrollX = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        ScrollY = ttk.Scrollbar(TableFrame, orient=VERTICAL)

        self.StudentTable = ttk.Treeview(TableFrame, columns=('Department', 'Course', 'Year', 'Semester', 'Studen ID', 'Student Name', 'Class Devision',
                                         'Roll No', 'Gender', 'DOB', 'Email ID', 'Mobile No', 'Address', 'Teacher', 'Photo'), xscrollcommand=ScrollX.set, yscrollcommand=ScrollY.set)

        ScrollX.pack(side=BOTTOM, fill=X)
        ScrollY.pack(side=RIGHT, fill=Y)
        ScrollX.config(command=self.StudentTable.xview)
        ScrollY.config(command=self.StudentTable.yview)

        self.StudentTable.heading('Department', text='Department')
        self.StudentTable.heading('Course', text='Course')
        self.StudentTable.heading('Year', text='Year')
        self.StudentTable.heading('Semester', text='Semester')
        self.StudentTable.heading('Studen ID', text='Studen ID')
        self.StudentTable.heading('Student Name', text='Student Name')
        self.StudentTable.heading('Class Devision', text='Class Devision')
        self.StudentTable.heading('Roll No', text='Roll No')
        self.StudentTable.heading('Gender', text='Gender')
        self.StudentTable.heading('DOB', text='DOB')
        self.StudentTable.heading('Email ID', text='Email ID')
        self.StudentTable.heading('Mobile No', text='Mobile No')
        self.StudentTable.heading('Address', text='Address')
        self.StudentTable.heading('Teacher', text='Teacher')
        self.StudentTable.heading('Photo', text='Photo sample')
        self.StudentTable['show'] = 'headings'

        self.StudentTable.column('Department', width=100)
        self.StudentTable.column('Course', width=100)
        self.StudentTable.column('Semester', width=100)
        self.StudentTable.column('Year', width=100)
        self.StudentTable.column('Studen ID', width=100)
        self.StudentTable.column('Student Name', width=100)
        self.StudentTable.column('Class Devision', width=100)
        self.StudentTable.column('Roll No', width=100)
        self.StudentTable.column('Gender', width=100)
        self.StudentTable.column('DOB', width=100)
        self.StudentTable.column('Email ID', width=100)
        self.StudentTable.column('Mobile No', width=100)
        self.StudentTable.column('Address', width=100)
        self.StudentTable.column('Teacher', width=100)
        self.StudentTable.column('Photo', width=100)

        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease>", self.GetCursor)
        self.FetchData()
    # ============Insert data=============

    def AddData(self):
        if self.departmentComboV.get() == "Select Department" or self.StudentidEnteryV.get() == '' or self.StudentNameEntryV.get() == '':
            messagebox.showerror('Error', 'All filed required')
        else:
            try:
                conn = mysql.connector.connect(
                    user='root', password='password', host='localhost', database='testdb')
                MyCursor = conn.cursor()
                MyCursor.execute('insert into facerecognition values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (self.departmentComboV.get(),
                                                                                                                      self.CourseComboV.get(),
                                                                                                                      self.YearComboV.get(),
                                                                                                                      self.SemesterComboV.get(),
                                                                                                                      self.StudentidEnteryV.get(),
                                                                                                                      self.StudentNameEntryV.get(),
                                                                                                                      self.ClassEnteryV.get(),
                                                                                                                      self.RollnoEntryV.get(),
                                                                                                                      self.GenderEnteryV.get(),
                                                                                                                      self.DOBEntryV.get(),
                                                                                                                      self.EmailEntryV.get(),
                                                                                                                      self.MobilenoEntryV.get(),
                                                                                                                      self.AddressEnteryV.get(),
                                                                                                                      self.TeacherEntryV.get(),
                                                                                                                      self.radio.get()))
                conn.commit()
                self.FetchData()
                conn.close()
                messagebox.showinfo(
                    'Sucess', 'Student details add Successfully', parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    'Error', f'Due to= {str(es)}', parent=self.root)

    # =============Fetch Data=============
    def FetchData(self):
        conn = mysql.connector.connect(
            user='root', password='password', host='localhost', database='testdb')
        MyCursor = conn.cursor()
        MyCursor.execute('select * from facerecognition')
        record = MyCursor.fetchall()
        if len(record) != 0:
            self.StudentTable.delete(*self.StudentTable.get_children())
            for i in record:
                self.StudentTable.insert('', END, values=i)
            conn.commit()
        conn.close

        # ===========Get cursor============
    def GetCursor(self, event=''):
        cursor_focus = self.StudentTable.focus()
        content = self.StudentTable.item(cursor_focus)
        record = content['values']
        self.departmentComboV.set(record[0]),
        self.CourseComboV.set(record[1]),
        self.YearComboV.set(record[2]),
        self.SemesterComboV.set(record[3]),
        self.StudentidEnteryV.set(record[4]),
        self.StudentNameEntryV.set(record[5]),
        self.ClassEnteryV.set(record[6]),
        self.RollnoEntryV.set(record[7]),
        self.GenderEnteryV.set(record[8]),
        self.DOBEntryV.set(record[9]),
        self.EmailEntryV.set(record[10]),
        self.MobilenoEntryV.set(record[11]),
        self.AddressEnteryV.set(record[12]),
        self.TeacherEntryV.set(record[13]),
        self.radio.set(record[14])

    # =========update data========
    def updateData(self):
        if self.departmentComboV.get() == "Select Department" or self.StudentidEnteryV.get() == '' or self.StudentNameEntryV.get() == '':
            messagebox.showerror(
                'Error', 'All filed required', parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    'Update', 'Do you want to update this student details', parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        user='root', password='password', host='localhost', database='testdb')
                    MyCursor = conn.cursor()
                    MyCursor.execute('update facerecognition set Department=%s,Course=%s,Year = %s,Semester=%s,StudentName=%s,Class=%s,RollNo=%s,Gender=%s,DOB=%s,EmailID=%s,MobileNo=%s,Address=%s,Teachar=%s,PhotoSample=%s where StudentID=%s', (self.departmentComboV.get(),
                                                                                                                                                                                                                                      self.CourseComboV.get(),
                                                                                                                                                                                                                                      self.YearComboV.get(),
                                                                                                                                                                                                                                      self.SemesterComboV.get(),
                                                                                                                                                                                                                                      self.StudentNameEntryV.get(),
                                                                                                                                                                                                                                      self.ClassEnteryV.get(),
                                                                                                                                                                                                                                      self.RollnoEntryV.get(),
                                                                                                                                                                                                                                      self.GenderEnteryV.get(),
                                                                                                                                                                                                                                      self.DOBEntryV.get(),
                                                                                                                                                                                                                                      self.EmailEntryV.get(),
                                                                                                                                                                                                                                      self.MobilenoEntryV.get(),
                                                                                                                                                                                                                                      self.AddressEnteryV.get(),
                                                                                                                                                                                                                                      self.TeacherEntryV.get(),
                                                                                                                                                                                                                                      self.radio.get(),
                                                                                                                                                                                                                                      self.StudentidEnteryV.get()))
                else:
                    if not update:
                        return
                messagebox.showinfo('Success','Studen details successfully updated',parent=self.root)
                conn.commit()
                self.FetchData()
                conn.close()                                                                                                                                                                                                       
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    #==========Delete function===========
    def deleteData(self):
        if self.StudentNameEntryV.get()=='':
            messagebox.showerror('Error','Student ID must be required',parent=self.root)
        else:
            try:
                delete=messagebox.askyesno('Student delete page','Do you wants to Delete this Student details.',parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                    user='root', password='password', host='localhost', database='testdb')
                    MyCursor = conn.cursor()
                    MyCursor.execute('DELETE FROM facerecognition WHERE StudentID=%s',(self.StudentidEnteryV.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.FetchData()
                conn.close()
                messagebox.showinfo('Delete','Student details successfully Deteled')
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
    # ========Resetm function========
    def resetData(self):
        self.departmentComboV.set('Select Department'),
        self.CourseComboV.set('Select Course'),
        self.YearComboV.set('Select Year'),
        self.SemesterComboV.set('Select Semester'),
        self.StudentidEnteryV.set(''),
        self.StudentNameEntryV.set(''),
        self.ClassEnteryV.set('Select Division'),
        self.RollnoEntryV.set(''),
        self.GenderEnteryV.set('Male'),
        self.DOBEntryV.set(''),
        self.EmailEntryV.set(''),
        self.MobilenoEntryV.set(''),
        self.AddressEnteryV.set(''),
        self.TeacherEntryV.set(''),
        self.radio.set('')
    #=============Generate data set or take photo samples============
    def generateDataset(self):
        if self.departmentComboV.get() == "Select Department" or self.StudentidEnteryV.get() == '' or self.StudentNameEntryV.get() == '':
            messagebox.showerror('Error', 'All filed required')
        else:
            try:
                conn = mysql.connector.connect(
                    user='root', password='password', host='localhost', database='testdb')
                MyCursor = conn.cursor()
                MyCursor.execute('select * from facerecognition')
                record=MyCursor.fetchall()
                id=0
                for x in record:
                    id+=1   
                MyCursor.execute('update facerecognition set Department=%s,Course=%s,Year = %s,Semester=%s,StudentName=%s,Class=%s,RollNo=%s,Gender=%s,DOB=%s,EmailID=%s,MobileNo=%s,Address=%s,Teachar=%s,PhotoSample=%s where StudentID=%s', (self.departmentComboV.get(),
                                                                                                                                                                                                                                      self.CourseComboV.get(),
                                                                                                                                                                                                                                      self.YearComboV.get(),
                                                                                                                                                                                                                                      self.SemesterComboV.get(),
                                                                                                                                                                                                                                      self.StudentNameEntryV.get(),
                                                                                                                                                                                                                                      self.ClassEnteryV.get(),
                                                                                                                                                                                                                                      self.RollnoEntryV.get(),
                                                                                                                                                                                                                                      self.GenderEnteryV.get(),
                                                                                                                                                                                                                                      self.DOBEntryV.get(),
                                                                                                                                                                                                                                      self.EmailEntryV.get(),
                                                                                                                                                                                                                                      self.MobilenoEntryV.get(),
                                                                                                                                                                                                                                      self.AddressEnteryV.get(),
                                                                                                                                                                                                                                      self.TeacherEntryV.get(),
                                                                                                                                                                                                                                      self.radio.get(),
                                                                                                                                                                                                                                      self.StudentidEnteryV.get()==id+1))
                conn.commit()
                self.FetchData
                self.resetData
                conn.close()
            # ================Load prefiend data on face frontal from openCV===============                                                                                                                                                              

                faceClassifier=cv.CascadeClassifier(r'D:\MyPythonProgramming\Face detection attendance system\haarcascade_frontalface_alt.xml')

                def face_cropped(img):
                    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                    faces=faceClassifier.detectMultiScale(gray,1.1,4)
                    # scaling factor = 1.1
                    # minimum neighbor = 4

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                webcam=cv.VideoCapture(0)
                img_id=0
                while True:
                    isTrue,myFrame=webcam.read()
                    if face_cropped(myFrame) is not None:
                        img_id+=1
                    # face=cv.resize(face_cropped(myFrame),(450,450))
                    face=cv.cvtColor(myFrame,cv.COLOR_BGR2GRAY)
                    fileName_path='D:/MyPythonProgramming/Face detection attendance system/photosample/user.'+str(id)+'.'+str(img_id)+'.jpg'
                    cv.imwrite(fileName_path,face)
                    cv.putText(face,str(img_id),(50,50),cv.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)  
                    cv.imshow('Cropped Face', face)
                    if cv.waitKey(1)==13 or int(img_id)==100:
                        break
                webcam.release()
                cv.destroyAllWindows()
                messagebox.showinfo('Result','Generating Data set completed')
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    def search(self):
        # print('no problem')
        conn = mysql.connector.connect(user='root', password='password', host='localhost', database='testdb')
        MyCursor = conn.cursor()
        a=self.searchV.get().replace(" ","")
        MyCursor.execute("select * from facerecognition where "+a+" Like'%"+str(self.searchEntryV.get())+"%'")
        record = MyCursor.fetchall()
        if len(record) != 0:
            self.StudentTable.delete(*self.StudentTable.get_children())
            for i in record:
                self.StudentTable.insert('', END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    app = Students(root)
    root.mainloop()
