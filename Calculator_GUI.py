import tkinter as tk
root = tk.Tk()
root.title('Standard Calculator')
root.resizable(0,0)

e = tk.Entry(root,width=35,bg='#f0ffff',fg='black',borderwidth=5,justify='right',font='Calibri 15')
e.grid(row=0,column=0,columnspan=3,padx=12,pady=12)

def buttonClick(num):
    temp = e.get()
    e.delete(0,tk.END)
    e.insert(0,temp + num)

def buttonClear():
    e.delete(0,tk.END)
