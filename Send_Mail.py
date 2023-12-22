import smtplib
from datetime import datetime,timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import sys
import cv2

def send_mail(frame):
    path = os.path.dirname(sys.argv[0])
    log_file = path + '/email.log'
    if os.path.isfile(log_file):
        with open(log_file,'r') as f:
            date = f.read()
            date_to_datetime = datetime.strptime(date,"%Y-%m-%d%H:%M:%S.%f")
            if datetime.now() < date_to_datetime + timedelta(minutes=1):
                return
        with open(log_file,'w') as f:
            f.write(str(datetime.now()))

        cv2.imwrite("intrude.jpg",frame)
        gmail_user = 'Enter_gmail-ID_to_be_used_for_sending_the_email'
        gmail_password = 'Enter_gmail-ID_password_here'
        recipient = 'Enter_gmailID_of_the_recipient'
        recipient = 'Enter_gmailID_of_the_recipient'
        message = 'Hey! It appears that someone is at home!!!'
        msg = MIMEMultipart()
