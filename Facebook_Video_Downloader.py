import time
from tkinter.ttk import *
import tkinter as tk
from requests import get, HTTPError, ConnectionError
from re import findall
from urllib.parse import unquote
from threading import Thread
import queue
from queue import Empty

def Invalid_Url():
    Status["text"] = "Invalid URL....."
    Status["fg"] = "red"

def get_downloadlink(url):
    url = url.replace("www","mbasic")
    try:
        r = get(url,timeout=5,allow_redirects=True)
        if r.status_code != 200:
            raise HTTPError
        a = findall("/video_redirect/",r.text)
        if len(a) == 0:
            print("[!] Video Not Found...")
            exit(0)

