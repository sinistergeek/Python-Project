import logging
import requests
import re
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import itertools
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import decouple

logging.basicConfig(format='%(asctime)s=%(name)s-%(levelname)s -%(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = decouple.config("API_KEY")

def start(update,context):
    update.message.reply_text('What can this bot do?\n\n This bot gives brief information about any moview from IMDB website' + '\n Send /name movie_name to know the genre and rating of the movie.Send genre genre_name to' + 'get the list of movies belonging to that genere')

def help(update,context):
    update.message.reply_text("Help!")

def genre(update,context):
    url = requests.get(url+'?genres='+genre)
    soup = BeautifulSoup(r.text,"html.parser")
    title = soup.find('title')
    if title.string == 'IMDB: Advanced Title Search - IMDb':
        update.message.reply_text("Sorry,No such genre.Try again")
    else:
        res = []
        res.append(title.string+"\n")
        tags = soup('a')
        for tag in tags:
            movie = re.search('<a herf=\"/title/.*>(.*?)</a>',str(tag))
            try:
                if "&amp;" in movie.group(1):
                    movie.group(1).replace("&amp;","&")
                res.append(movie.group(1))
            except:
                pass

str = ""
for i in res:
    stri += i +'\n'
update.message.reply_text(stri)


def name(update,context):
    movie = str(update.message.text)[6:]
    print(movie)
    res = get_info(movie)
    stri = ""
    for i in res:
        for a in i:
            stri += a + "\n"
        stri += '\n'
    update.message.reply_text(stri)

def error(update,context):
    logger.warning('Update "%s" caused error "%s"',update,context.error)

def get_info(movie):
    url = 'https://www.imdb.com/find?q='
    r =requests.get(url+movie+'&ref_=nv_sr_sm')
    soup = BeautifulSoup(r.text,"html.parser")
    title = soup.find('title')
    tags = soup('a')
    pre_url = ""
    count = 0
    lis = []
    res = []
    for tag in tags:
        if(count > 2):
            break
        m re.search('<a her=.*>(.?)</a>',str(tag))
        try:
            list = []
            link = re.search('/title/(.*?)/',str(m))
            new_url = 'https://www.imdb.com' + str(link.group(0))
            if new_url != pre_url:
                html = requests.get(new_url)
                soup2 = BeautifulSoup(html.text,"html.parser")

