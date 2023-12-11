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


def buttonGet(oper):
    global num1,math
    num1 = e.get()
    math = oper
    e.insert(tk.END,math)
    try:
        num1 = float(num1)

    except ValueError:
        buttonClear()

def buttonEqual():
    inp = e.get()
    num2 = float(inp[inp.index(math) + 1:])
    e.delete(0,tk.END)
    if math == '+':
        e.insert(0,str(num1 + num2))
    elif math == '-':
        e.insert(0,str(num1 - num2))
