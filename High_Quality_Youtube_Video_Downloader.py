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
        if i == 1:
            if text2.get()!='paste link 2 here...':
                pro2.start()
                download(text2.get())
                pro2.destroy()
                lable2 = Label(root,text='completed!').grid(row=1,column=1)
        if i == 2:
            if text3.get() != 'paste link 3 here..':
                pro3.start()
                download(text3.get())
                pro3.destroy()
                lable3 = Label(root,text='completed!').grid(row=2,column=1)


        if i==3:
            if text4.get() != 'paste link 4 here...':
                pro4.start()
                download(text4.get())
                pro4.destroy()
                label4 = Label(root,text='completed!').grid(row=3,column=1)



