from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://www.instagram.com")
time.sleep(10)

username = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(input("Enter your username:"))
print("Enter your Password: ")
password = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
paswd = getpass()
password.send_keys(pswd)
login_button = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login_button.click()
time.sleep(10)
search_bar = chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
