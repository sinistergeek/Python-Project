import logging
from json.decoder import JSONDecodeError
from pathlib import Path
import pandas as pd
import requests
from requests.exceptions import ProxyError

logging.basicConfig(level=logging.INFO)

def add_proxies_to_file(csv_path:str,proxies: list):
    if not csv_path.exists():
        pr_file:pd.DataFrame = pd.DataFrame(columns=['proxy_type','proxy_address','proxy_status'])
        logging.info('New CSv file will be created')
    else:
        pr_file:pd.DataFrame = pd.read_csv(csv_path)
        logging.info('Existing CSV file has been loaded')


    for proxy in proxies:
        if len(pr_file) == 0:
            pr_file = pr_file.append(proxy,ignore_index=True)
        else:
            if len(pr_file.loc[(pr_file['proxy_type'] == proxy['proxy_type'])&(pr_file['proxy_address'] == proxy['proxy_address']) ]) > 0:
                pr_file.loc[(pr_file['proxy_type'] == proxy['proxy_type']) &(pr_file['proxy_address'] == proxy['proxy_address']),['proxy_status']] = proxy['proxy_status']

            else:
                pr_file = pr_file.append(proxy,igonre_index=True)

    pr_file = pr_file.drop_duplicates()
    pr_file.to_csv(csv_path,index=False)
    logging.info('CSv file has been written')

def test_proxy(proxy_type:str,proxy_address:str,iptest:str):
    logging.info(f'Testing proxy: {proxy_address}')
    try:
        proxies = {proxy_type:proxy_address}
        proxy_status:str=''

        if proxy_type=='https':
            r=requests.get(f'https://{iptest}',proxies=proxies)

        else:
            r= requests.get(f'http://{iptest}',proxies=proxies)

        try:
            json_response:dict = r.json()
            if json_response["ip"] in proxy_address:
                proxy_status = 'Proxy functional'
            else:
                logging.warning(f'Proxy"{proxy_address}"' f'returned{json_response}')
                proxy_status = 'Proxy not functional'

        except JSONDecodeError:
            proxy_status = 'Invalid response'

    except ProxyError:
        proxy_status = 'Proxy Error'

    logging.info(f'Proxy {proxy_address} : {proxy_status}')
    return {'proxy_type':proxy_type,'proxy_address':proxy_address,'proxy_status':proxy_status}

def test_single_proxy(proxy:str,iptest:str,csv_path:str):
    proxy_type,proxy_address = proxy.split('://')
    result:dict = test_proxy(proxy_type,proxy_address,iptest)
    add_proxies_to_file(Path(csv_path),[result])


def test_csv_file(iptest:str,csv_path:str):
    csv_path:Path =Path(csv_path)
    if csv_path.exists():
        pr_file:pd.DataFrame = pd.read_csv(csv_path)
    else:
        raise FileNotFoundError
    proxies: list = []
    for index,proxy in pr_file.iterrows():
        proxies.append(test_proxy(proxy['proxy_type'],proxy['proxy_address'],iptest))
        add_proxies_to_file(csv_path,proxies)

def add_from_text_file(iptest:str,text_path:str,csv_path:str):
    text_path:Path = Path(text_path)
    if text_path.exists():
        proxies: list = text_path.read_text().splitlines()
        for proxy in proxies:
            test_single_proxy(proxy,iptest,csv_path)

    else:
        raise FileNotFoundError
