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

    elif math == 'x':
        e.insert(0,str(num1 * num2))
    elif math == '/':
        try:
            e.insert(0,str(num1/num2))
        except ZeroDivisionError:
            e.insert(0,'Undefined')

b1 = tk.Button(root,text='1',padx=40,pady=10,command=lambda:buttonClick('1'),font='Calibri 12')
b2 = tk.Button(root,text='2',padx=40,pady=10,command=lambda:buttonClick('2'),font='Calibri 12')
b3 = tk.Button(root,text='3',padx=40,pady=10,command=lambda:buttonClick('3'),font='Calibri 12')
b4 = tk.Button(root,text='4',padx=40,pady=10,command=lambda:buttonClick('4'),font='Calibri 12')
b5 = tk.Button(root,text='5',padx=40,pady=10,command=lambda:buttonClick('5'),font='Calibri 12')
b6 = tk.Button(root,text='6',padx=40,pady=10,command=lambda:buttonClick('6'),font='Calibri 12')
b7 = tk.Button(root,text='7',padx=40,pady=10,command=lambda:buttonClick('7'),font='Calibri 12')
b8 = tk.Button(root,text='8',padx=40,pady=10,command=lambda:buttonClick('8'),font='Calibri 12')
b9 = tk.Button(root,text='9',padx=40,pady=10,command=lambda:buttonClick('9'),font='Calibri 12')
b0 = tk.Button(root,text='0',padx=40,pady=10,command=lambda:buttonClick('0'),font='Calibri 12')
bdot = tk.Button(root,text='.',padx=41,pady=10,command=lambda:buttonClick('.'),font='Calibri 12')
badd = tk.Button(root,text='+',padx=29,pady=10,command=lambda:buttonGet('+'),font='Calibri 12')
bsub = tk.Button(root,text='-',padx=30,pady=10,command=lambda:buttonGet('-'),font='Calibri 12')
bmul = tk.Button(root,text='x',padx=30,pady=10,command=lambda:buttonGet('x'),font='Calibri 12')
bdiv = tk.Button(root,text='/',padx=30.5,pady=10,command=lambda:buttonClear,font'Calibri 12')
bclear = tk.Button(root,text='AC',padx=20,pady=10,command=buttonClear,font='Calibri 12')
bequal = tk.Button(root,text='=',padx=39,pady=10,command=buttonEqual,font='Calibri 12')

b1.grid(row=3,coloumn=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
badd.grid(row=3,column=3)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
bmul.grid(row=2,column=3)
