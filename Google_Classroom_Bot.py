from selenium import webdriver
from time import sleep
from configparser import ConfigParser
from datetime import datetime
import csv

config = ConfigParser()
config.read('config.ini')
username = config.get('AUTH','USERNAME')
password = config.get('AUTH','PASSWORD')
classTime=["09:20","11:40","14:25"]

class ClassAutomation():
    def __init__(self):
        self.count=0
        self.findCount()
        while True:
            if datetime.now().strftime("%H:%M") in classTime:
                print(datetime.now().strftime("%H:%M"))
                self.initClass()
            sleep(30)
    def initClass(self):
        className = self.findClass()
        if className is None:
            return
        print("Initiating...")
        self.login()
        self.driver.find_element_by_xpath("//div[text()='{}']".format(className)).click()
        sleep(10)
        link = self.driver_element_by_partial_link_text("https://meet.google.com/lookup/").text
        self.driver.get(link)
        sleep(10)
        self.driver.find_element_by_xpath("//span[text()='Joinnow']").click()
        sleep(60*60)
        print("Qutting...")
        sleep(5)
        slef.driver.quit()
        if self.count < 2:
            self.count = self.count + 1
        else:
            self.count = 0
        self.findCount()

    def findClass(self):
        with open("schedule.csv","r") as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if row["Day"] == datetime.now().strftime("%a"):
                    return row[classTime[self.count]]
            return None
    def findCount(self):
        if self.findClass() is None:
            print("No Class Today")
            return
        currentTime = datetime.now().strftime("%H:%M")
