import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
categories = {'Most Runs':'most-runs','Most Fours':'most-fours','Most Sixes':'most-sixes','Most Fifties':'most-fifties','Most Centuries':'most-centuries','Highest Scores':'highest-score','Most Wickets':'most-wickets','Most Maidens':'most-maidens','Most Dot Balls':'most-dot-balls','Best Bowling Average':'best-bowling-average','Best Bowling Average':'best-bowling-average','Best Bowling Economy':'best-bowling-economy','Best Bowling Strike Rate':'best-bowling-strike-rate'}
def generate_url():
    category_choice = category.get()
    year_choice = year.get()
    if(year_choice  == 'All time'):
        year_choice = 'all-time'

    category_slug = categories[category_choice]
    url = 'https://www.iplt20.com/stat/{}/{}'.format(year_choice,category_slug)
    return url

def scrapte_results():
    url = generate_url()
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find("table",{"class": "table table--scroll-on-tablet top-players"})
    row = results.findChildren('tr')
    table_data = []
    row_values = []
