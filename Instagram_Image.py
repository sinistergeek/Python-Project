from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep,strftime
from random import randint
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
import requests as rq
webdriver = webdriver.Chrome()
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(20)

