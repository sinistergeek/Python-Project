from selenium import webdriver
import requests as rq
import os
from bs4 import BeautifulSoup
import time

path = input("Enter Path:")
url = input("Enter URL:")
output = "output"

def get_url(path,url):
    driver = webdriver.Chrome(executable_path=r"{}".format(path))
    driver.get(url)
    print("loading.....")
    res = driver.execute_script("return document.documentElement.outerHTML")
    return res
def get_img_links(res):
    soup = BeautiifulSoup(res,"lxml")
    imglinks = soup.find_all("img",src=True)
    return imglinks

def download_img(img_link,index):
    try:
        extensions = [".jpeg",".jpg",".png",".gif"]
        extension = ".jpg"
        for exe in extensions:
            if img_link.find(exe) > 0:
                extension = exe
                break
            imag_data = rq.get(img_link).content
            with open(output + "\\" + str(index + 1) + extension, "wb+") as f:
                f.write(img_data)
                f.close()
    except Exception:
        pass

