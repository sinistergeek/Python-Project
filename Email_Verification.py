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
