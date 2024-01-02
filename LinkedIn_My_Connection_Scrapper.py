from selenium.webdriver.common.action_chains import ActionChains
from optparse import OptionParser
from selenium import webdriver
import pandas as pd
import time
import sys
import re

pattern_name = "\\n(.+)\\n"
pattern_headline = 'occupation\\n(.+)\\n'
usage="""
<Script> [Options]
[Options]
-h,--help show this help message and exit.
-e,--email Enter login email
-p,--password Enter login password
-s,--skills Flag to scrap each profile, and look at its skill set

operation Modes:
    >Basic mode
    This will scrap all LinkedIn connections list with threre corresponding Name,Headline,and Profile link.
    >Skills scrapper mode(-s/--skills)
    (Time Consuming mode)
    This will do the same job of basic mode but along with visiting each profile and extacting the skills of each.
"""

parser = OptionParser()
parser.add_option("-e","--email",dest="email",help="Enter login email")
parser.add_option("-p","--password",dest="password",help="Enter loging password")
parser.add_option("-s","--skills",action="store_true",dest="skills",help="Flag to scrap each profile, and look at its skill set")
def login(email,password):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.linkedin.com")
    session_key = driver.find_element_by_name("session_key")
    session_key.send_keys(email)
    session_password = driver.find_element_by_name("session_password")
    session_password.send_keys(password)
    submit = driver.find_element_by_class_name("sigin-in-form__submit-button")

