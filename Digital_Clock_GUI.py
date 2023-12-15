from tkinter import Label,Tk
import time
app_window =Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font=("Boulder",68,'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label = Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)
