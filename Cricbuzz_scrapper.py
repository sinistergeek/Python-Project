from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time


URL = 'http://www.cribuzz.com/cricket-match/live=scores'

def notify(title,score):
    toaster = ToastNotifier()
    toaster.show_toast("CRICKET LIVE SCORE",score,duration=30,icon_path='ipl.co')

while True:
    request = Request(URL,headers={'User-Agent':'XYZ/3.0'})
    response = urlopen(request,timeout=20).read()
    data_content = response
    soup = BeautifulSoup(data_content,'html.parser')

    update[]
    for score in soup.find_all('div',attrs={'class': 'cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main'}):
        header = score.find('div', attrs={'class':'cb-col-100 cb-col cb-shdl'})
        header = header.text.strip()
        status = score.find('div',attrs={'class':'cb-scr-will-chvrn cb-lv-scrs-col'})
        s= status.text.strip()
        notify(header,s)
        time.sleep(10)

