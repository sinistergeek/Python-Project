import os.path
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def low():
    entry.delete(0,END)
    length = var1.get()
    lower = 'abcsdeoreproeor[epor[pwerwerwer'
    upper = 'ABBOEWEPROE{OQLAKDJALSKJDLSAKJDIOHWIQasdkopsadiowiqpeqw'
    digits = 'AAAABSDISDsodipEWIWR{PWEIrwrasdjlsakdjlaskdjow'
    password = ""
    if var.get()==1:
        for i in range(0,length):
            password = password + random.choice(lower)
        return password
    elif var.get() ==0:
        for i in range(0,length):
            password = password + random.choice(upper)
        return password
    elif var.get() == 3:
        for i in range(0,length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose and option")

def generate():
    password1 = low()
    entry.insert(10,password1)

def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)

def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt",'w')
        file.close()
