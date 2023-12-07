import csv
from email.message import emailMessage
import smtplib

def get_credentials(filepath):
    with open("credentails.txt","r") as f:
        email_address = f.readline()
        email_pass = f.readlines()

    return(email_address,email_pass)

def login(email_address,email_pass,s):
    s.ehlo()
    s.startls()
    s.ehlo()
    s.login(email_address,email_pass)
    print("login")


def send_mail():
    s = smtplib.SMTP("smtp.gmail.com",587)
    email_address,email_pass = get_credentials("./credentials.txt")

    login(email_address,email_pass,s)
    subject = "Wellcome to Python"
    body = """ Python is an interpreted,hight-level,general-purpose programming language.\n CReated by Guido van Rossum and first released in 1991,Python's design philosophy emphasizes code readbility\nwith its notable use of significant whitespace
    """
    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = subject

    with open("emails.csv",newline="") as csvfile:
        spamreader = csv.reader(csvfile,delimiter="",quotechar="|")
        for email in spamreader:
            s.send_message(email_address,email[0],message)
            print("Send To" + email[0])

            s.quit()
            print(send)

if __name__ == "__main__":
    send_mail()
