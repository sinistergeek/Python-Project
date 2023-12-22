import argparse
import hashlib

parser = argparse.ArgumentParser(description='hasing given password')
parser.add_argument('password',help='input password you want to hash')
parser.add_argument('-t','--type',default='sha256',choices=['sha256','sha512','md5'])
args = parser.parse_args()
password = args.password
hashtype =args.type
m = getattr(hashlib,hashtype)()
m.update(password.encode())
print("<hash-type:"+hashtype + ">")
print(m.hexdigest())
