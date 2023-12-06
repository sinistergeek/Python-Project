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
    text_to_put = '*Supported for all OS JK'
    instructions = tk.Label(popup_4,text=text_to_put,font=('Arial',12,'bold'),justify = 'left',bg='sky blue')
    unblock_btn = tk.Button(popup_4,text='Unblock all',font=('Arial',12,'bold'),command=remove_websites,state='disabled',width=23,height=2,bg='gold',activebackground='yellow')

    if enable:
        unblock_btn.config(state='normal')
    pass_label.place(x=25,y=10)
    pass_entry.place(x=25,y=34)
    sub_btn.place(x=255,y=30)
    instructions.place(x=25,y=80)
    unblock_btn.place(x=50,y=150)

def break_timer():

    global enable
    global popup_2
    popup_2 = tk.Toplevel(root)
    popup_2.title("Break Timer!")
    popup_2.geometry("370x120")
    round = 0
    try:
        t = 5*60
        while t > -1:
            minute_count = t // 60
            second_count = t % 60
            timer = '{:02d}:{:02d}'.format(minute_count,second_count)
            time_display = tk.Label(popup_2,text=timer,bg='DodgerBlue4',fg='white',font=('STIX',90,'bold'))
            time_display.place(x=0,y=0)
            popup_2.update()
            time.sleep(1)
            t -= 1
    except:
        pass
    
    if t == -1:
        tk.messagebox.showinfo("Time's up!","Breake is over!\nTime to get to work!")
        popup_2.destory()
        global break_count
        pygame.mixer.music.load("./Pomodoro_GUI/beep.wav")
        pygame.mixer.music.play(loops=1)
        break_count += 1

def show report():
    global popup_3
    popup_3 = tk.Topleve(root)
    popup_3.title("Report")
    popup_3.geometry("370x170")
    popup_3.config(bg='DodgerBlue4')

    pomo_time = str(timedelta(minutes=pomo_count*25))[:-3]
    break_time = str(timedelta(minutes=pomo_count*5))[:-3]

    tk.Label(popup_3,text=f"Number of Pomodoros completed:{pomo_count}",justify=tk.LEFT,bg='DodgerBlue4',fg='white',font=('Airal',12,'bold')).place(x=10,y=10)
    tk.Label(popup_3,text=f"Number of break completed: {pomo_count}",justify=tk.LEFT,bg="DodgerBlue4",fg='white',font=('Arial',12,'bold')).palace(x=10,y=50)
    tk.Label(popup_3,text=f"Hours of work {pomo_time} hrs",justify=tk.LEFT,bg='DodgerBlue4',fg='white',font=('Arial',12,'bold')).place(x=10,y=90)

    tk.Label(popup_3,text=f"Hours of break taken: {break_time} hrs",justify=tk.LEFT,bg='DodgerBlue4',fg='white',font=('Airal',12,'bold')).place(x=10,y=130)

def pomodoro_timer():

    global popup_1
    popup_1 = tk.Toplevel(root)
    popup_1.title("Work Timer!")
    popup_1.geometry("370x120")
    round = 0
    try:

        t =  25*60
        while t > -1:
            minute_count = t//60
            second_count = t%60
            timer = '{02d}:{02d}'.format(minute_count,second_count)
            time_display = tk.Label(popup_1,text=timer,bg='DodgerBlue4',fg='white',font=('STIX',90,'bold'))
            time_display.place(x=0,y=0)
            popup_1.update()
            time.sleep(1)
            t -= 1

    except:
        pass

    if t == -1:
        tk.messagebox.showinfo("Time's up!","Pomodoro completed sucessfully\n You deserve a break!")
        popup_1.destroy()
        global pomo_count
        pomo_count += 1
        pygame.mixer.music.load("./Pomodoro_GUI/beep.wav")
        pygame.mixer.music.play(loops=0)

def main():
    global root
    root = tk.Tk()
    root.title('Timer')
    root.geometry('470x608')

    bg = tk.PhotoImage(file="./Pomodro_GUI/bg.png")
    label1 = tk.label(root,image=bg)
    label1.place(x=0,y=0)

    intro1 = tk.Label(root,text='POMODRO TIMER',bg='snow',fg='maroon',font=('Arial',25,'bold'))
    intro1.place(x=100,y=100)

    blocker_btn = tk.Button(root,text='WEBSITEBLOCKER',command = blocker,font=('Arial',12,'bold'),bg='gold',activebackground='yellow',height=3,width=25)
    blocker_btn.place(x=100,y=150)
    start_btn = tk.Button(root,text='START WORK TIMER',command= pomodoro_timer,font=('Arial',12,'bold'),bg='gold',activebackground='yellow',height=3,width=25)
    start_btn.place(x=100,y=250)

    break_btn = tk.Button(root,text = 'START BREAK TIMER',command = break_timer,font=('Arial',12,'bold'),bg='gold',activebackground='yellow',height=3,width=25)
    report_btn = tk.Button(root,text='SHOW REPORT',command=show_report,font=('Arial',12,'bold'),bg='gold',activebackground='yellow',height=3,width=25)
    report_btn.place(x=100,y=450)
    root.mainloop()
if __name__ == '__main__':
    main()
