import pandas as pd
import datetime
import smtplib
import os

current_path = os.getcwd()
print(current_path)
os.chdir(current_path)
GMAIL_ID = input("Enter your email:")
GMAIL_PSWD = input("Enter Password for your email mentioned above:")


