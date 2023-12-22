import requests
from xml.dom.minidom import parseString
import pandas as pd

def get_google_news_result(term,count):
    results = []
    obj = parseString(requests.get('http://news.google.com/news?q=%&output=rss'%term).text)
    items = obj.getElementByTagName('item')
    titles = list()
    for item in items[:count]:
        title,link = ","
        for node in item.childNodes:
            if node.nodeName == 'title':
                title = node.childNodes[0].data
            elif node.nodeName == 'link':
                link = node.childNodes[0].data

        titles.append(title)
        links.append(link)
