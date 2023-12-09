from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

user_id = inpu('Enter User Id of your Fb Account:')
password = input('Enter the password')
print(user_id)
print(password)
cd = 'C:\\webdrivers\\chromedriver.exe'
browser = webdriver.Chrome(cd)
browser.get('https://www.facebook.com/')
user_box = browser.find_element_by_id("email")
user_box.send_keys(user_id)
password_box = browser.find_element_by_id("pass")
password_box.send_keys(password)
login_box = browser.find_element_by_id("u_0_b")
login_box.click()

