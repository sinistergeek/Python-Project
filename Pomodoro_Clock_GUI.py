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


