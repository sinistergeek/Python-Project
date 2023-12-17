from dns import resolver
import smtplib
import socket
import re

def check_syntax(email):
    regex=r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):
        print("Check 1 (Syntax) Passed")
    else:
        print("Check 1 FAILED! Bad Syntax,Invalid Email!")
        exit()

def check_dns(email,domain):
    try:
        records = resolver.resolve(domain,'MX')
        mxRecord =str(records[0].exchange)
        print("Check 2 (DNS - ",mxRecord+") Passed")
        return mxRecord
    except:
        print("Check 2 FAILED! The domain",domain,"does not exist,Invalid Email!")
        exit()

def check_response(email,domain,mxRecord):
    try:
        host = socket.gethostname()
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(mxRecord)
        server.helo(host)
        server.mail(email)
        code,message=server.recpt(str(email))
        if codef == 250:
            print("Check 3(SMTP response) Passed")
            print(email,"is a VALID email address!")
        else:
            print("Check 3 FAILED! The user",email.split("@")[0],"does not exist,Invalid Email!")
    except socket.error as socketerror:
        print("Check 3 HALTEd! The domain",domain,"either does not have an SMTP or have restricted access through external scripts")
email = input("Enter your Email id:")
domain = email.split("@")[-1]
check_syntax(email)
mxRecord = check_dns(email,domain)
check_response(email,domain,mxRecord)
