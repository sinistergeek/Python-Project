import hashlib
import pyAesCrypt
import random
import os,time
import shutil

import email,smtplib,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

buffer=64*1024

while buffer!=0:
    print('*******FIle EncRypt0R*******')
    print("This is a OPEN Source AES Standard encryption tool")
    print('****************************')
    print('1.Encrypt\n2.Decrypt\n3.Folder Encryption\n4.Folder Decryption \n5.Contact us \n6.Exit')
    ip = int(input('Enter options:'))
    if ip == 1:
        fname = input(str('Enter file path(without quotes):'))

        try:
            sub_key="abcdefg!~hijklm#$&*nopqrstuvw-+@xyz02345+/67890A-)(%BCDEFGHIJKLMNOPQRSTUVWXYZ"
            enc_key = "".join(random.sample(sub_key,30))
            pyAesCrypt.encryptFile(fname,fname+'.aes',enc_key,buffer)
            os.remove(fname)
            print("-------------Encryption Sucessfull---------\n \n User Warning: Make sure to notedown the encryption keys,failure to do so the data cannot be reverted back ever again.")
            print('\n Encryption Key:',enc_key+'\n')
            now = time.strftime("%H:%M")
            with open('C:\\Interl\\'+'temp_key.txt','a+') as f:
                f.write(fname + '|||' +now+ '|||' +enc_key+'\n')
            time.sleep(10)

        except:
            print('Invalid File \n')
    elif ip==2:
        try:
            fname = input(str('Enter file path:'))
            if fname[-4:] == '.aes':
                key = input(str('Enter our decryption key:'))
                pyAesCrypt.decryptFile(fname,'Out_'+fname[:-4],key,buffer)
                os.remove(fname)
                print('Decyrption Succesfull...')
                time.sleep(5)

            else:
                print('Invalid Crypto-File\n')

        except:
            print('Decryption Failed....\n')
    elif p==3:
        fol = input('Enter the folder path(without quotes):')
        if not os.path.exists('encrypted_folder'):
            os.mkdir('encrypted_folder')
            sub_key="abcdefg!~hijklm#$&*nopqrstuvw-+@xyz02345+/67890A-)(%BCDEFGHIJKLMNOPQRSTUVWXYZ"
            enc_key = "".join(random.sample(sub_key,30))
            for i in os.listdir(fol):
                if i[-4:]!='.aes'
                try:
