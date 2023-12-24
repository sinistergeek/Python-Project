from selenium import webdriver
import time
from webdriver_manager.chrom import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(10)
users = list(map(str,input("Enter Users Username Comma-Separated Whom You Want to Follow and Send Msg").split(",")))
USERNAME = input("Enter Your Username")
PASSWORD = input("Enter Your Password")
browser.get('https://www.instagram.com/')
wait = WebDriverWait(browser,120)
time.sleep(2)
