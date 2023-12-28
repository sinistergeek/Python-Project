from tqdm import tqdm
import requests
import re
from PIL import Image
def pp_download(username):
    url = "https://www.instagram.com/{}/".format(username)
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com',url)
    if x:
        check_url1 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/].*\?hl=[a-z-]{2,5}', url)
        check_url2 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com$|^(https:)[/][/]www.([^/]+[.])*instagram.com/$', url)
        check_url3 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/][a-zA-Z0-9_]{1,}$', url)
        check_url4 = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com[/][a-zA-Z0-9_]{1,}[/]$', url)

    if check_url3:
        final_url = url + '/?__a=1'
