from selenium import webdriver
from email_validator import validate_email,EmailNotValidError
import csv


def LinkedInEmailScraper(userEmail,userPassword):
    emailList = {}
    browser = webdriver.Chrome()
    url = '[INSERT URL TO LINKEDIN POST]'
    browser.get(url)
    browser.implicity_wait(5)

