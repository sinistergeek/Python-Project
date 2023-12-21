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

