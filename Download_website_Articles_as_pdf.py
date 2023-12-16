from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import requests

def get_driver():
    chrome_options = webdriver.ChromeOptions()
    settings = {
            "recentDestinations":[{"id":"Save as PDF","origin":"local","account":""}],"selectedDestinationId":"Save as PDF","version":2}
    prefs = {"printing.print_preview_sticky_settings.appState":json.dumps(settings)}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument("--kiosk-printing")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)
    return browser
