from selenium import webdriver
from email_validator import validate_email,EmailNotValidError
import csv


def LinkedInEmailScraper(userEmail,userPassword):
    emailList = {}
    browser = webdriver.Chrome()
    url = '[INSERT URL TO LINKEDIN POST]'
    browser.get(url)
    browser.implicity_wait(5)
    commentDiv = browser.find_element_by_xpath('/html/body/main/section[1]/section[1]/div/div[3]/a[2]')
    loginLink = commentDiv.get_attriute('href')
    browser.get(loginLink)
