from bs4 import BeautifulSoup
import requests as req

currencies = []

page = req.get('https://www.x-rates.com/').text
#print(page)

soup = BeautifulSoup(page,'html.parser')
#print(soup)
options = soup.find_all('option')[:-11]
#print(options)

for option in options:
    currency_short = option.text[:(option.text.find(""))]
    currency_name = option.text[(option.text.find("")+3):]
    current_element = {'name':currency_name,'short':currency_short}
    currencies.append(current_element)
    print('{}.{}({})'.format(len(currencies),current_element['name'],current_element['short']))
    currency_index = int(input('Enter your currency\'s position number:'))
    currency = currencies[currency_index]

