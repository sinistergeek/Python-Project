import tkinter as tk
from tkinter import filedialog
from PIL import Image
root=tk.Tk()
root.title('Converter')
canvas1 = tk.Convas(root,width=300,height=250,bg='orange',relief='raised')
canvas1.pack()
label1 = tk.Label(root,text='File Converter',bg='lightsteelblue2')
label1.config(font=('helvetica',20))
canvas1.create_window(150,60,window=label1)
im1=None
