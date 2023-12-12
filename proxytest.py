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
