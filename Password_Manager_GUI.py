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
