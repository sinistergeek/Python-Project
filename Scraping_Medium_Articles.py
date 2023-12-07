import os
import sys
import requests
import re
from bs4 import BeautifulSoup

os.chdri('\\'.join(__file__.split('/')[:-1]))

def get_page():
    global url
    url = input('Enter url of a medium article:')

    if not re.match(r'https?://medium.com',url):
        print('Please enter a valid website, or make sure it is a medium article')
        sys.exit(1)
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text,'html.parser')
        return soup
