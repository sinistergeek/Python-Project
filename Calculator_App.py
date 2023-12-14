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

def popupmsg():
    popup = Tk()
    popup.resizable(0,0)
    popup.geometry("120x100")
    popup.title("Alert")
    label = Label(popup,text="Cannot divide by 0! \n Enter valid values")
    label.pack(side="top",fill="x",pady=10)
    B1 = Button(popup,text="Okay",bg="#DDDDDD",command=popup.destory)
    B1.pack()

def cal():
    root = Tk()
    root.title("Calc")
    root.resizable(0,0)

    entry_font = font.Font(size=15)
    entry=Entry(root,justify="right",font=entry_font)
    entry.grid(row=0,column=0,columnspan=4,sticky=N + W + S + E, padx=5,pady=5)

