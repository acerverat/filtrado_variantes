# !/usr/bin/python3
# Importing dependencies
from tkinter import *

from tkinter.filedialog import askopenfilename

# Running interface
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file
filename = askopenfilename()
print(filename)
