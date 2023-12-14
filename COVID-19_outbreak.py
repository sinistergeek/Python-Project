from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notify_user(title,message):
    notification.notify(title=title,message=message,app_icon="./Covid-19_Real-time_Notification/Notify_icon.icon",timeout=5)

def getInfo(url):
    r = requests.get(url)
    return r.text



if __name__ == '__main__':
    t = int(input("Enter interval in secs:"))
    li = list(map(str,input("Enter name of states: ").split(",")))
    states=[]

