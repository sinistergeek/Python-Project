import urllib.request,urllib.parse,urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

