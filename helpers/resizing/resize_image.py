import tkinter as tk
from PIL import Image, ImageTk

class ImageLabel(tk.Label):
    def __init__(self, parent, **kwargs):
        path = kwargs.pop('path', None) 
        if path is not None:
            image  = Image.open(path) 

            resize = kwargs.pop('resize', None)
            if resize is not None:
                image = image.resize(resize, Image.LANCZOS) 

            # Keep a reference to prevent garbage collection
            self.photo = ImageTk.PhotoImage(image)
            kwargs['image'] = self.photo

        super().__init__(parent, **kwargs)