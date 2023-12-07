from bs4 import BeautifulSoup
import requests
import csv

url = 'http://quotes.toscrape.com'

html = requests.get(url)
bs = BeautifulSoup(html.text,'html.parser')


try:
    csv_file = open('quote_list.csv','w')
    fieldnames=['quote','author','tags']
    dictwriter = csv.DictWriter(csv_file,fieldnames=fieldnames)

    dictwriter.writeheader()

