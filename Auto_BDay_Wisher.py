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

if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for index,item in df.iterrows():
        bday = item['Birthday']
        bday = datetime.datetime.strptime(bday,"%d-%m-%Y")
        bday = bday.strftime("%d-%m")
        if(today == bday) and yearNow not in str(item['LastWishedYear']):
            sendEmail(item['Email'],"Happy Birthday",item['Dialogue'])
            writeInd.append(index)

    if writeInd != None:
        for i in writeInd:
            oldYear = df.loc[i,'LastWishedYear']
            df.loc[i,'LastWishedYear'] = str(oldYear) + "," + str(yearNow)
    df.to_excel('data.xlsx',index=False)
