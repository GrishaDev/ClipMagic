# Clip Magic

Extended clipboard for windows and linux.
Not tested on linux yet, might not work at all :O


## Guide

Everytime you press ctrl c, the application will add it to list of extended clipboard.
Pressing ctrl + alt + 1-9  will choose clipboard from the list.
Pressing ctrl + alt + 0  will hide the window and run the application in background, pressing again
will show the window again.


### getting exe

Python used: 3.5

pip this and other stuff that needed.

```
pip install cx_Freeze
```

cx_freeze used to get exe


cd to directory of everything and run

```
python setup.py build
```

this will create in same directory a build folder.
You will get exe inside (: