from tkinter import *
import calendar

def showCal():

    box = Tk()
    box.title("Calendar For The Year")
    box.geometry("550x600")
    find_year = int(year_field.get())
    first_label = Label(box,text='CALENdAR', bg='dark grey', font=("times",28,'bold'))
    first_label.grid(row=1,column=1)
    box.config(background="white")
    cal_data = calendar.calendar(find_year)
    cal_year = Label(box,text=cal_data,font="consolas 10 bold",justify=LEFT)
    cal_year.grid(row=2,column=1,padx=20)

    box.mainloop()
