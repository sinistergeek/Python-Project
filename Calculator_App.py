from tkinter import Tk,END,Entry,N,E,S,W,Button
from tkinter import font
from tkinter import Label
from functools import partial

def get_input(entry,argu):
    entry.insert(END,argu)

def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

def clear(entry):
    entry.delete(0,END)

def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDvivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(END,output)


