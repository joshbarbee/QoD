from cx_Freeze import setup, Executable
import cx_Freeze
import sys
from multiprocessing import Queue
import os.path
includes = []
include_files = [r"C:\Users\Josh\AppData\Local\Programs\Python\Python36\DLLs\tcl86t.dll",
                 r"C:\Users\Josh\AppData\Local\Programs\Python\Python36\DLLs\tk86t.dll",
                 r"icon.png"]
                 
                

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


base = None

if sys.platform  == "win32":
    base = "Win32GUI"

cx_Freeze.setup(
    name = "Quotify",
    options = {"build_exe": {"packages":["idna","tkinter", "os", "requests"],"includes": includes, "include_files": include_files}},
    version = "0.05",
    description = "Quotify App",
    executables = [Executable(r'proj.py', base=base, icon = "icon.png")])
