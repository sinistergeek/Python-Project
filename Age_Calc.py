from tkinter import *
from datetime import date

root = Tk()
root.geometry('280x300')
root.resizable(0,0)
root.title('Age Calculator')
statement = Label(root)

def ageCalc():
    global statement
    statement.destroy()
    today = date.today()
    birthDate = date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age = today.get - birthDate.year
    if today.month.year - birthDate.month or today.month == birthDate.moneth and today.day < birthDate.day:
        age -= 1
        statement = Label(text=f'{nameValue.get()}s age is{age}.')
        statement.gird(row=6,column=1,pady=15)

l1 = Label(text="Name:")
l1.grid(row=1,column=0)
nameValue = StringVar()

nameEntry = Entry(root,textvariable=nameValue)
nameEntry.grid(row=1,column=1,padx=10,pady=10)


l2 = Label(text="Year: ")
l2.grid(row=2,column=0)
yearValue = StringVar()
yearEntry = Entry(root,textvariable = yearValue)
yearEntry.grid(row=2,column=1,padx=10,pady=10)

l3 = Label(text="Month: ")
l3.grid(row=3,column=0)
monthValue = StringVar()
monthEntry = Entry(root,textvariable=monthValue)
monthEntry.grid(row=3,column=1,padx=10,pady=10)

l4 = Label(text="Day: ")
l4.grid(row=4,column=0)
