from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import youtube_dl
import os

root =tk.Tk()
root.title('Youtube downloader V-2.3')
root.geometry("350x140")
root.config(bg='#dfe6e9')
ydl_opts = {}
def shutcom():
    global key
    key = 0
    buttonshut = tk.Button(root,text="yes",command=shutcom,state=DISABLED,bg='#dfe6e9',fg='#f2f2f2')
    buttonshut.grid(row=4,column=1)

def download(link):
    link_of_the_video = link
    zxt = link_of_the_video.strip()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])


def downloadall():
    for i in range(4):
        if i == 0:
            if text1.get()!='paste link 1 here...':
                pro1.start()
                download(text1.get())
                pro1.destroy()
                label1=Label(root,text='completed!').grid(row=0,column=1)
                
