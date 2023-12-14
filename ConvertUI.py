import tkinter as tk
from PIL import Image
root = tk.Tk()
img = None
font = ('helvetica',12,'bold')
bg = 'blue'
fg = 'white'
width = 15

def getPNG():
    global img
    import_file_path = tk.filedialog.askopenfilename(filetypes=[("PNG File",'.png')])
    img = Image.open(import_file_path)

def convertToICO():
    global img
    if img is None:
        tk.messagebox.showerror("Error","No File selected")

    else:
        export_file_path=tk.filedialog.asksaveasfilename(defaultextension='.ico')
        img.save(export_file_path)
        tk.messagebox.showinfo("Success","File converted and saved")

root.title('PNG to ICO Converter')
canvas1 = tk.Canvas(root,width=500,height=350,bg='lgihtblue')
canvas1.pack()
label1 = tk.Label(root,text='PNG to ICO Converter',bg='lightblue')
label1.config(font=('helvetica',20))
canvas1.create_window(250,100,window=label1)
browseButton = tk.Button(text="Import PNG File",command=getPNG,bg=bg,fg=fg,font=font,width=width)
