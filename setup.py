import sys
from cx_Freeze import setup, Executable

setup(name="clipmagic",
      version="1",
      description="Extended clipboard",
      executables=[Executable("clip.py", base=None)])

#"Win32GUI"