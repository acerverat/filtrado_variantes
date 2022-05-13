# !/usr/bin/python3

# from helpers.browser.open import open_cosmic_webpage
# from helpers.downloads.download_variants import download
# from helpers.archives.open_files import *
# from scripts.run_analysis import run_comparison, show_results

# Importing dependencies
from tkinter import PhotoImage, filedialog, Text, Label, Entry
from PIL import ImageTk, Image
import webbrowser
import os
import tkinter as tk

# Running interface
window = tk.Tk()

window.title("COSMIC Browser")
# Setting up canvas
canvas = tk.Canvas(window, height=800, width=1000, bg="#01244D")
canvas.pack()

# Setting up frame
# iconphoto=PhotoImage(file='../public/dna.jpg')
home = tk.Frame(window, bg="white")
home.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.25)

# Importing images
inmegen_logo = Image.open("../public/inmegen_logo.jpg")
cosmic_logo = Image.open("../public/cosmicLogo.jpg")

# Resize the Image using resize method
inmegen_resized  = inmegen_logo.resize((150, 150), Image.ANTIALIAS)
cosmic_resized  = cosmic_logo.resize((600, 100), Image.ANTIALIAS)

inmegen_logo_resized = ImageTk.PhotoImage(inmegen_resized)
cosmic_logo_resized = ImageTk.PhotoImage(cosmic_resized)

inmegen = tk.Label(image=inmegen_logo_resized)
inmegen.image = inmegen_logo_resized

cosmic = tk.Label(image=cosmic_logo_resized)
cosmic.image = cosmic_logo_resized


# Position image
inmegen.place(x=450, y=30)
cosmic.place(x=250, y=300)

# Title
Text(home, text="InMeGen", font="Arial 20 bold", bg="white").place(x=0, y=0)

# Labels
Label(home, text="Email").place(x=200, y=200)
Label(home, text="Password").place(x=200, y=225)

# Text input
email = Entry(home, width=40, borderwidth=3).place(x=300, y=200)

password = Entry(home, width=40, borderwidth=3, show='*').place(x=300, y=225)

# Declaring files
files = []

# TODO: Move all aux functions to helpers
# Auxiliary functions


def get_file():
    for widget in home.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(
        initialdir="../../", title="Selecciona el archivo", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    files.append(filename)
    print(filename)
    for app in files:
        label = tk.Label(home, text=app, bg="gray")
        label.pack()


def get_folder():
    for widget in home.winfo_children():
        widget.destroy()
    folder = filedialog.askdirectory(
        initialdir="../../", title="Selecciona la carpeta")
    files.append(folder)
    print(folder)
    for app in files:
        label = tk.Label(home, text=app, bg="gray")
        label.pack()


def open_cosmic_webpage():
    webbrowser.open('https://cancer.sanger.ac.uk/cosmic/register', new=2)


def download():
    print(f"")
    print("Downloading cosmic variants...")


def run_comparison():
    for file in files:
        os.startfile(file)


def show_results():
    print("Showing results...")


# Setting up buttons
cosmic_webpage = tk.Button(window, text="Registrate en Cosmic", padx=10,
                           pady=5, fg="white", bg="#01244D", command=open_cosmic_webpage)

cosmic_variants = tk.Button(window, text="Descarga variantes cancerigenas", padx=10,
                            pady=5, fg="white", bg="#01244D", command=download)


open_file = tk.Button(window, text="Selecciona archivos de un pacientes", padx=10,
                      pady=5, fg="white", bg="#01244D", command=get_file)

open_folder = tk.Button(window, text="Selecciona carpeta con pacientes", padx=10,
                        pady=5, fg="white", bg="#01244D", command=get_folder)


run_analysis = tk.Button(window, text="Corre el analisis", padx=10,
                         pady=5, fg="white", bg="#01244D", command=run_comparison)

results = tk.Button(window, text="Ver resultados", padx=10,
                    pady=5, fg="white", bg="#01244D", command=show_results)

cosmic_webpage.pack()
cosmic_variants.pack()
open_file.pack()
open_folder.pack()
run_analysis.pack()
results.pack()

window.mainloop()

# The interface should have two fields to write the email and pass
# The interface should have a text box that displays the results of the analysis.
# The interface should have a button to save the results to a file.
