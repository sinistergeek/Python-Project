import pyautogui
import time
import webbrowser
from selenium import webdriver
from time import sleep
from webdriver_manager.chrom import ChromeDriverManager
from getpass import getpass


LOGIN_URL = 'https://www.facebook.com/login.php'
num = str(input("Enter group ids separated by commas:"))
lists = num.split(",")
groupid = []
for i in lists:
    groupid.append(i)
    message = input("Enter your message:")


class FacebookLogin():
    def __init__(self,email,password,browser='Chrome'):
        self.email = email
        self.password = password
        if browser == 'Chrome':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            seelf.driver.get(LOGIN_URL)
            time.sleep(1)

    def login(self):
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email)
        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password)
        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click()

        time.sleep(2)

        for i in range(len(groupid)):
            link = 'https://facebook.com/groups/'+groupid[i]
            self.driver.get(link)
            print("Waiting for few seconds ...")
            time.sleep(45)

            self.driver.find_element_by_class_name('a8c37x1j ni8dbmo4 stjgntxs 19j0dhe7').click()
            time.sleep(7)

            self.driver.switch_to.active_element.send_keys("message")
            time.sleep(7)


            self.driver.find_element_by_class_name('a8c37x1j ni8dbmo4 stjgntxs 19j0dhe7 ltmttdrg g0qnabr5').click()
            time.sleep(7)


if __name__ == '__main__':

    usr = input('Enter Email Id:')
    pwd = getpass('Enter Password:')
    fb_login = FacebookLogin(email=usr,password=pwd,browser='Chrome')
    fb_login.login()
