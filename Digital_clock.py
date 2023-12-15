import tkinter as tk
from time import strftime

def light_theme():
    frame =tk.Frame(root,bg="white")
    frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    lbl_1 = tk.Label(fra,e.font=('calibri',40,'bold'),background='White',foreground='black')
    lbl_1.pack(anchor="s")



def time():
    string =strftime('%I:%M:%S:%p')
    lbl_1.config(text=string)
    lbl_1.after(1000,time)

time()

def dark_theme():
    frame = tk.Frame(root,bg="#22478a")
    frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    lbl_2 =tk.Label(frame,font=('calibri',40,'bold'),background='#22478a',foreground='black')
    lbl_2.pack(anchor="s")

def time():
    string = strftime('%I:%M:%S %p')
    lbl_2.config(text=string)
    lbl_2.after(1000,time)

time()
