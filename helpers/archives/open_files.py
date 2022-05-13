# !/usr/bin/python3
from tkinter import filedialog, Text
import tkinter as tk

# files = []

# def get_file(frame):
#     for widget in frame.winfo_children():
#         widget.destroy()
#     filename = filedialog.askopenfilename(
#         initialdir="../../", title="Selecciona el archivo", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
#     files.append(filename)
#     print(filename)
#     for app in files:
#         label = tk.Label(frame, text=app, bg="gray")
#         label.pack()
        
# def get_folder(frame):
#     for widget in frame.winfo_children():
#         widget.destroy()
#     folder = filedialog.askdirectory(
#         initialdir="../../", title="Selecciona la carpeta")
#     files.append(folder)
#     print(folder)
#     for app in files:
#         label = tk.Label(frame, text=app, bg="gray")
#         label.pack()