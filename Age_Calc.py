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
