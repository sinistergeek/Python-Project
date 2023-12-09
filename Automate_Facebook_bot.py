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
