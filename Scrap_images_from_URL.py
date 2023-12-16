from selenium import webdriver
import requests as rq
import os
from bs4 import BeautifulSoup
import time

path = input("Enter Path:")
url = input("Enter URL:")
output = "output"

