import os
import requests
url="https://graph.facebook.com/{}/picture?type=large"
path = os.getcwd()

if not "fb_dps" in os.listdir(path):
    os.mkdir("fb_dps")
