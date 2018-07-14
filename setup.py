import sys
from cx_Freeze import setup, Executable

setup(name="clipmagic",
      version="1",
      description="Extended clipboard",
      options={'build_exe': {'packages': ["jaraco"]}},
      executables=[Executable("clip.py", base=None)])

#"Win32GUI"