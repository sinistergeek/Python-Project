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
    for row in rows:
        cells = row.findChildren(['th','td'])
        for cell in cells:
            value = cell.text.strip()
            value = " ".join(value.split())
            row_values.append(value)
        table_data.append(row_values)
        row_values = []

    p_records = ""
    for player in table_data[:51]:
        single_record = ""
        for cell in player:
            format_cell = "{:<20}"
            single_record += format_cell.format(cell[:20])
        single_record += "\n"
        p_records += single_record


    query_label.config(state=tk.NORMAL)
    query_label.delete(1.0,"end")
    query_label.insert(1.0,p_records)
    query_label.config(state=tk.DISABLED)

