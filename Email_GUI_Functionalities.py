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

