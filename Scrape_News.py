import requests
import os
from bs4 import BeautifulSoup,SoupStrainer

if not os.path.exists(os.path.join(os.getcwd(),'HackerNews')):
    os.makedirs(os.path.join(os.getcwd(),'HackerNews'))


def fetch(page_no,verbose=False):
    if page_no <=0:
        raise ValueError('Number of pages must be greater than zero')

    page_no = min(page_no,20)
    i=page_no
    if verbose:
        print('Fetching Page{}..'.format(i))
