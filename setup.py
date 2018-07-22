import sys
from cx_Freeze import setup, Executable
# import os
# os.environ['TCL_LIBRARY'] = "C:\\Users\\Grisha\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tcl8.6"
# os.environ['TK_LIBRARY'] = "C:\\Users\\Grisha\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tk8.6"
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="clipmagic",
      version="1",
      description="Extended clipboard",
      options={'build_exe': {'packages': ["jaraco", "tkinter"],'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ]}},
      executables=[Executable("clip.py", base=base)])

#"Win32GUI"