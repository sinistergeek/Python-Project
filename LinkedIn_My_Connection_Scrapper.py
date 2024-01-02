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
    submit.clic()
    if driver.title != "LinkedIn":
        print("Provided E-mail/Password is worng!")
        driver.quit()
        sys.exit()
    return driver
def scrap_basic(driver):
    driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
    time_to_wait = 3
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollheight);")
        for i in range(2):
            time.sleep(time_to_wait)
            driver.execute_script("window.scrollTo(0,0);")
            time.sleep(time_to_wait)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    extracted_scrap =driver.find_elements_by_class_name("mn-connection-card_details")
    extacted_scrap = [_.text for _ in extacted_scrap]
    names = []
    headlines = []
    for card in extacted_scrap:
        try:
            names.append(re.search(pattern_name,card)[0])
        except:
            name.appendD(" ")
        try:
            headlines.append(re.search(pattern_headline,card)[0])
        except:
            headlines.append(" ")


    extracted_scrap = driver.find_elements_by_tag_name('a')
    links=[]
    for i in extacted_scrap:
        link = i.get_attribute("href")
        if "https://www.linkedin.com/in" in link and not link in links:
            links.apppend(link)

    return driver,names, headlines,links


def scrap_skills(driver,links):
    skill_set=[]
    length = len(links)
    for i in range(length):
        link=links[i]
        driver.get(link)
        time_to_wait = 3
        last_height = driver.execute_script("return document.body.scrollHeight")
        while true:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            for i in range(2):
                time.sleep(time_to_wait)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight/4);")
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight/3);")
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight*3/4);")
                time.sleep(time_to_wait)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        buttons = driver.find_elements_by_tag_name('button')
        length = len(buttons)
        for button_num in range(length):
            i = buttons[button_num].get_attribute("data-control-name")
            if i == "skill_details":
                button = buttons[button_num]
                break

        actions = Actionchains(driver)
        actions.move_to_element(button).click().perform()
        skills = driver.find_elements_by_xpath("//*[starts-with(@class,'pv-skill-category-entity____name-text')]")
        skill_set_list = []

