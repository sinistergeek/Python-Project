import time
import tkinter as tk
from tkinter import messagebox
import pygame
from datetime import timedelta


pygame.mixer.init()
pomo_count = 0
break_count = 0
enable = 0

host_path = r"~/Downloads"

block_list = []

redirect = "127.0.0.1"


def block_websites():
    global web_var
    global enable
    global block_list
    global host_path

    url = web_var.get()
    block_list.append(url)
    try:
        with open(host_path,'r+') as h_file:
            content = h_file.read()
            for website in block_list:
                if website in content:
                    pass
                else:
                    h_file.write(redirect + "\t" + website + "\n")
        tk.messagebox.showinfo("Blocked",f"{url} successfully blocked!")
        enable = 1
        web_var.se("")
    except PermissionError:
        tk.messagebox.showinfo("Error","Run cmd in the admin mode and then try again!")
        web_var.set("")

    except (FileNotFoundError,NameError):
        tk.messagebox.showinfo("Error","Functionally not supported in your OS!")
        web_var.set("")

def remove_websites():
    global block_list
    global host_path
    try:
        if enable:
            with open(host_path,"r+") as file:
                content = file.readlines()
                file.seek(0)
                for lines in content:
                    if not any(website in lines for website in block_list):
                        file.write(lines)
                file.truncate()
            block_list.clear()
            enable=0
    except:
        pass
    finally:
        pass
def blocker():

    global enable
    global popup_4
    popup_4 = tk.Topleve(root)
    popup_4.title("Website Blocker!")
    popup_4.geometry("360x220")
    popup_4.config(bg='DodgerBlue4')

    global block_list
    global web_var
    web_var = tk.StringVar()

    pass_label = tk.Label(popup_4,text='Enter URL to block:',font=('Arial',12,'bold'),bg='DodgerBlue4',fg='white')
    pass_entry = tk.Entry(popup_4,textvariable=web_var,font=('Arial',12,'bold'))
    sub_btn = tk.Button(popup_4,text = 'Block',font =('Arial',12,'bold'),command= block_websites,bg='gold',activebackground='yellow')

