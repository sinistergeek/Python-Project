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
