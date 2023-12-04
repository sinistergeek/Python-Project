import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import front as tkFont
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = input('Enter path for chromedriver')

most_active = {'Most Active equities - Main Board':'mae_mainboard_tableC','Most Active equities - SME':'mae_sme_tableC','Most Active equities =ETFs':'mae_etf_tableC','Most Active equities - Price Spurts':'mae_pricespurts_tableC','Most Active equities - Volume Spurts':'mae_volumespurts_tableC'}

top_20 = {'NIFTY 50 Top 20 Gainers':'topgainer-Table','NIFTY 50 Top 20 Losers':'toplosers-Table'}

def generate_url():
    category_choice = category.get()
    if(category_choice in most_active):
        page = 'most-active-equities'
    else:
        page = 'top-gainers-loosers'
    url = 'https://www.nseindia.com/market-data/{}'.format(page)

    return url
def scraper():
    url = generate_url()
    driver = webdriver.Chrome(driver_path)
    driver.get(url)

    time.sleep(5)
    html = driver.page_source

    soup = BeautifulSoup(html,'html.parser')

    category_choice = category.get()

    if category_choice in most_active:
        category_div = most_active[category_choice]
    else:
        category_div = top_20[category_choice]

    result =soup.find("table",{"id": category_div})
    rows = result.findChildren('tr')

    table_data = []
    row_values = []
    
    for row in rows:
        cells = row.findChildren(['th','td'])
        for cell in cells:
            value = cell.text.strip()
            value = "".join(value.split())
            row_values.append(value)

        table_data.append(row_values)
        row_values = []
    stocks_data = ""
    for stock in table_data:
        single_record = ""
        for cell in stock:
            format_cell = "{:<20}"
            single_record += format_cell.format(cell[:20])
        single_record += "\n"
        stocks_data += single_record

    query_label.config(state=tk.NORMAL)
    query_label.delete(1.0,"end")
    query_label.insert(1.0,stocks_data)
    query_label.config(state=tk.DISABLED)
    driver.close()
    window = tk.Tk()
    window.title('NSE Stock data')
    window.geometry('1200x1000')
    windows.configure(bg='white')

style = ttk.Style()
style.configure('my.TButton',font=('Helvetica',16))
style.configure('my.TFrame',background='white')
ttk.Label(window,text="NSE Stock market data",background='white',foreground="SpringGreen2",font=("Helvetica",30,'bold')).grind(row=0,column=1)
ttk.label(window,text="Select Market data to get:",background='white',font=("Helvetica",15)).grind(column=0,row=5,padx=10,pady=25)
category = ttk.Combobox(window,width=60,state='readonly',font="Helvetica 15")

submit_btn = ttk.Button(window,text="Get Stock Data!",style='my.TButton',command=scraper)

category['values'] = ('Most Active equities - Main board','Most Active equities = SmE','Most Active equtieis ETFs','Most Active equities - Price Spurts','Most Active equties - Volume Spurts','NIFTY 50 Top 20 gainers','NIFTY 50 Top 20 Loser')

category.grid(column=1,row=5,padx=10)
category.current(0)

submit_btn.grind(row=5,column=3,pady=5,padx=15,ipadx=5)

frame = ttk.Frame(window,style='my.TFrame')
frame.place(relx= 0.50,rely=0.12,relwidth=0.98,relheight=0.90,anchor="n")

query_label = tk.Text(frame.height="52",width="500",bg="alice blue")
query_label.grid(row=7,columnspan=2)
window.mainloop()
