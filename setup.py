import cx_Freeze
import sys
import os
base= None

if sys.platform=='win32':
    base='win32GUI'

os.environ['TCL_LIBRARY'] =r'C:\Users\Chandrika Chundawat\AppData\Local\Programs\Python\Python39\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Chandrika Chundawat\AppData\Local\Programs\Python\Python39\tcl\tk8.6'

executables=[cx_Freeze.Executable('Login.py',base= base, icon='faceid3.ico')]

cx_Freeze.setup(
    name= 'Facial Recognition Software',
    options={'build_exe':{'packages':['tkinter','os'],'include_files':['faceid3.ico','tcl86t.dll','tk86t.dll','projectImage','dataBase','AttendanceReport','photosample']}},
    version='1.0',
    description = 'Face Recognition Automatic Attendace system | Devloped by Ankit sharma',
    executables=executables 
)
    