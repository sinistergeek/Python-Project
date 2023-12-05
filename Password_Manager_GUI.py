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

def hide():
    query_label['text'] = ""
    query_btn.configure(text="Show Records",command=lambda: query(con))
root = Tk()
root.title("Password Manager")
root.geometry("500x400")
root.minsize(600,400)
root.maxsize(600,400)

frame = Frame(root,bg="#744A9F",bd=5)
frame.place(relx=0.50,rely=0.50,relwidth=0.98,relheight=0.45,anchor="n")

website = Entry(root,width=30)
website.grid(row=1,column=1,padx=20,pady=5)
username = Entry(root,width=30)
username.grid(row=2,column=1,padx=20,pady=5)
password = Entry(root,width=30)
password.grid(row=3,column=1,padx=20,pady=5)

website_label = Label(root,text="Website:")
website_label.grid(row=1,column=0)
username_label = Label(root,text="Username")
username_label.grid(row=2,column=0)
password_label = Label(root,text="Password")
password_label.grid(row=3,column=0)


submit_btn = Button(root,text="Add Password",command=lambda:submit(con))
submit_btn.grid(row=5,column=1,pady=5,padx=15,ipadx=35)
query_btn = Button(root,text="Show Ali",command=lambda:query(con))
query_btn.grid(row=6,column=1,pady=5,padx=5,ipadx=35)

global query_label
query_label = Label(frame,anchor="nw",justify="left")
query_label.place(relwidth=1,relheight=1)

def main():
    root.mainloop()
if __name__ == '__main__':
    main()
