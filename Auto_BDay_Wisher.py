import pandas as pd
import datetime
import smtplib
import os

current_path = os.getcwd()
print(current_path)
os.chdir(current_path)
GMAIL_ID = input("Enter your email:")
GMAIL_PSWD = input("Enter Password for your email mentioned above:")

def sendEmail(to,sub,msg):
    print(f'Email to {to} send: \n Subject:{sub},\nMessage:{msg}')
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID,to,f"Subject: {sub} \n\n {msg}")
    s.quit()
