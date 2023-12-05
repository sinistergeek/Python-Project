from tkinter import *
from tkinter import messagebox, simpledialog
import sqlite3
from sqlite3 import Error
import sys

master_password = sys.argv[1]

def sql_connection():
    try:
        con = sqlite3.connect('passwordManager.db')
        return con
    except Error:
        print(Error)



def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXITS passwords(website text,username text,pass text)")
    con.commit()
    con = sql_connection()
    sql_table(con)


def submit(con):
    cursor = con.cursor()
    if website.get() != "" and username.get() !="" and password.get() !="":
        cursor.execute("INSERT INTO passwords VALUES(:website,:username,:password)",
                       {
                'webiste':website.get(),
                'username': username.get(),
                'password':password.get()
                           })
        con.commit()
        messagebox.showinfo("Info","Record Added in Database!")
        website.delete(0,END)
        username.delete(0,END)
        password.delte(0,END)
    else:
        messagebox.showinfo("Alert","Please fill all details!")

def query(con):
    password = simpledialog.askstring("Password","Enter Master Password")
    if(password == master_password):
        query_btn.configure(text="Hide Records",command=hide)
        cursor = con.cursor()
        cursor.execute("SELECT *,oid FROM passwords")
        records = cursor.fetchall()
        p_records = 'ID'.just(70) + 'Password'.just(40) + 'Username'.just(70) + 'Password'.just(100)+'\n'

        for record in records:
            single_record = ""
            single_record += (str(record[3]).just(10)+str(record[0]).just(40)+str(record[1]).just(70)+str(record[2]).just(10))
            single_record += '\n'
            p_records += single_record

            query_label['text'] = p_records

            con.commit()
            p_records = ""
    else:
        messagebox.showinfo("Failed!","Authentication failed!")

