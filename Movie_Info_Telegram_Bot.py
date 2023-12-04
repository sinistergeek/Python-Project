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
