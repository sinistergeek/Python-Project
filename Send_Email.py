import smtplib
import csv
from string import Template
from email.mine.multipart import MIMEMultipart
from email.mine.text import MIMEText
def read_template(filename):
    with open(filename,'r',encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    message_template = read_template('template.txt')
    MY_ADDRESS ='*****@gmail.com'
    PASSWORD = '********'
    s = smtplib.SMTP(host='smtp.gmail.com',port=587)
    s.startls()
    s.login(MY_ADDRESS,PASSWORD)

    with open('details.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        next(csv_reader)
        for lines in csv_reader:
            msg = MIMEMultipart()
            message = message_template.substitute(PERSON_NAME=row[0],MATH=row[2],ENG=row[3],SCI=row[4])
            msg['From'] = MY_ADDRESS
            msg['To'] = lines[1]
            msg['Subject'] = "Mid term grades"
            msg.attach(MIMEText(message,'plain'))
            s.send_message(msg)
            del msg
            s.quit()

if __name__ =='__main__':
    main()
