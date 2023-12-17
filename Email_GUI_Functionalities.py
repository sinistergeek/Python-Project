import smtplib
from tkinter import *

def send_message():
    address_info = address.get()
    email_body_info = enail_body.get()
    sender_info = sender_address.get()
    password_info = password.get()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_info,password_info)
    print("Login successful")
    server.sendmail(sender_info,address_info,email_body_info)
    print("Message sent")
    address_entry.delete(0,END)
    email_body_entry.delete(0,END)
    password_entry.delete(0,END)
    sender_address_entry.delete(0,END)

gui = Tk()
gui.geometry("500x500")
gui.titl("Email Sender App")
heading = Label(text="Email Sender App",bg="yellow",fg="black",font="10",width="500",height="3")
heading.pack()
gui.configure(background="light blue")
sender_address_field = Label(text="Sender's Email :")
sender_address_field.place(x=15,y=70)
sender_address = StringVar()
sender_address_entry = Entry(textvariable = sender_address,width="30")
sender_address_entry.place(x=15,y=100)
sender_password_field = Label(text="Sender's Password:")
sender_password_field.place(x=15,y=140)
password = StringVar()

