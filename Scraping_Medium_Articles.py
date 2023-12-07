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

def puriy(text):
    rep = {"<br>":"\n","<br/>":"\n","<li>":"\n"}
    rep = dict((re.escape(k),v) for k,v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))],text)
    text = re.sub('\<(.*?)\>','',text)
    return text

def collect_text(soup):
    fin = f'url:{url}\n\n'
    main = (soup.head.title.text).split('|')
    global title
    title = main[0].strip()
    fin += f'Title:{title.upper()}\n{main[1].strip()}'
    header = soup.find_all('h1')
    j=1
    try:
        fin +='\n\nINTRODUCTION\n'
        for elem in list(header[j].previous_siblings)[::-1]:
            fin += f'\n{purify(str(elem))}'
    except:
        pass
    fin +=f'\n\n{header[j].text.upper()}'
    for elem in header[j].next_siblings:
        if elem.name == 'h1':
            j+=1
            fin += f'\n\n{header[j].text.upper()}'
            continue
        fin += f'\n{purify(str(elem))}'
        return fin


