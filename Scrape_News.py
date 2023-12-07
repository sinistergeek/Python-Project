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

    try:
        res = requests.get('https://news.ycombinator.com/?p='+str(i))
        only_td = SoupStrainer('td')
        soup = BeautifulSoup(res.content,'html.parser',parse_only=only_td)
        tdtitle = soup.find_all('td',attrs={'class':'title'})
        tdmetrics = soup.find_all('td',attrs={'class':'subtext'})
        with open(os.path.join('HackerNews','NewsPage{}.txt'.format(i)),'w+') as f:
            f.write('-'*80)
            f.write('\n')
            f.write('Page {}'.format(i))
            tdtitle = soup.find_all('td',attrs={'class':'title'})
            tdrank = soup.find_all('td',attrs={'class':'title','align':'right'})
            tdtitleonly = [t for t in tdtitle if t not in tdrank]
            tdmetrics = soup.find_all('td',attrs={'class':'subtext'})
            tdt = tdtitleonly
            tdr = tdrank
            tdm = tdmetrics
            num_iter = min(len(tdr),len(tdt))
            for idx in range(num_iter):
                f.write('\n'+'-'*80+'\n')
                rank = tdr[idx].find('span',attrs={'class':'rank'})
                titl = tdt[idx].find('a',attrs={'class':'storylink'})
                url = titl['href'] if titl and titl['href'].startswith('https') else 'https://news.ycombinator.com/' + titl['href']
                site = tdt[idx].find('span',attrs={'class':'sitestr'})
                score = tdm[idx].find('span',attrs={'class':'score'})
                time = tdm[idx].find('span',attrs={'class':'age'})
                author = tdm[idx].find('a',attrs={'class':'hnuser'})
                f.write('\nArticle Number:'+ rank.text.replace('.') if rank else '\n Article Number: Could not get article number')
                f.write('\n Article Title:' + title.text if titl else '\nArticle Title: Could not get article title')
                f.write('\nSource Website' + site.text if site else '\nSource Website: https://news.ycombinator.com')
