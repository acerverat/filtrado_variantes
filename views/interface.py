# !/usr/bin/python3

# from helpers.browser.open import open_cosmic_webpage
# from helpers.downloads.download_variants import download
# from helpers.archives.open_files import *
# from scripts.run_analysis import run_comparison, show_results

# Importing dependencies
from tkinter import PhotoImage, filedialog, Message, Label, Entry
from PIL import ImageTk, Image
import requests
from requests.auth import HTTPBasicAuth
import webbrowser
import tkinter as tk
import os
import zipfile

# TODO: finish watching https://www.youtube.com/watch?v=TuLxsvK4svQ

# Running interface
window = tk.Tk()

window.title("Descubre pacientes con cancer")
# Setting up canvas
canvas = tk.Canvas(window, height=800, width=1000, bg="#01244D")
canvas.pack()

# Setting up frame
home = tk.Frame(window, bg="white")
home.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.25)

# Importing images
inmegen_logo = Image.open("../public/inmegen_logo.jpg")
cosmic_logo = Image.open("../public/cosmicLogo.jpg")

# Resize the Image using resize method
# TODO: https://stackoverflow.com/questions/58247550/resize-pil-image-valueerror-unknown-resampling-filter
inmegen_resized = inmegen_logo.resize((150, 150), Image.ANTIALIAS)
cosmic_resized = cosmic_logo.resize((600, 100), Image.ANTIALIAS)


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
title = Message(home, text="Hola! Deberas iniciar sesion en Cosmic para poder descargar las variantes, tras escribir tus credenciales porfavor dale click en \"Descarga variantes cancerigenas\".",
                width=500, bg="white", font=("Helvetica", 10))


# Labels
Label(home, text="Email").place(x=200, y=220)
Label(home, text="Password").place(x=200, y=245)

# Text input
email = Entry(home, width=40, borderwidth=3)

password = Entry(home, width=40, borderwidth=3, show='*')

# Declaring files
files = []
title.pack()
email.pack()
password.pack()
email.place(x=300, y=220)
password.place(x=300, y=245)

title.place(x=190, y=300)
# TODO: Move all aux functions to helpers
# Auxiliary functions

# Here we authenticate the user to download the variants

# async, await?


def download():
    # Extracting the email and password from the interface
    user_email = email.get()
    user_password = password.get()
    # Encryption of authentication
    # api-endpoint
    URL = "https://cancer.sanger.ac.uk/cosmic/file_download/GRCh38/cosmic/v95/CosmicMutantExport.tsv.gz"
    res = requests.get(url=URL, auth=HTTPBasicAuth(user_email, user_password))
    data = res.json()
    print(data.url)
    # file = await requests.get(url=data.url)
    # open('CosmicMutantExport.tsv.gz', 'wb').write(file.content)
    # TODO: https://stackoverflow.com/questions/3451111/unzipping-files-in-python
    # Defining a params dict for the parameters to be sent to the API
    print("Downloading...")


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


def run_comparison():
    for file in files:
        print(file)
    print("Running comparison...")


def show_results():
    print("Showing results...")


def testing():
    print("Testing...")


# Setting up buttons
cosmic_webpage = tk.Button(window, text="Registrate en Cosmic", padx=10,
                           pady=5, fg="white", bg="#01244D", command=open_cosmic_webpage)

cosmic_variants = tk.Button(window, text="Descarga variantes cancerigenas", padx=10,
                            pady=5, fg="white", bg="#01244D", command=download)


open_file = tk.Button(window, text="Selecciona archivos de pacientes", padx=10,
                      pady=5, fg="white", bg="#01244D", command=get_file)

open_folder = tk.Button(window, text="Selecciona carpeta con pacientes", padx=10,
                        pady=5, fg="white", bg="#01244D", command=get_folder)


run_analysis = tk.Button(window, text="Corre el analisis", padx=10,
                         pady=5, fg="white", bg="#01244D", command=run_comparison)

results = tk.Button(window, text="Ver resultados", padx=10,
                    pady=5, fg="white", bg="#01244D", command=show_results)

test_code = tk.Button(window, text="Test de funcionalidad", padx=10,
                      pady=5, fg="white", bg="#01244D", command=testing)

cosmic_webpage.pack()
cosmic_variants.pack()
open_file.pack()
open_folder.pack()
run_analysis.pack()
results.pack()
test_code.pack()

cosmic_webpage.place(x=450, y=410)
cosmic_variants.place(x=400, y=600)

window.mainloop()
