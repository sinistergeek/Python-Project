from selenium import webdriver
from time import sleep
import datetime
from prettytable import PrettyTable

start =datetime.datetime.now()
table=PrettyTable()
column_names = ["Non-Followers"]

class InstaBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.username=username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.url = self.driver.current_url
        if self.url == "https://www.isntagram.com/accounts/onetap/?next=%2F":
            self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
            sleep(4)
            self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

        else:
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
            sleep(1)
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        sleep(2)
        followers =self._get_names()
        notfollowingback = [user for user in following if user not in followers]
        table.add_column(column_names[0],notfollowingback)
        print(table)

