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

    if check_url4:
        final_url = url + '?__a=1'

    if check_url1:
        alpha = check_url1.group()
        final_url = re.sub('\\?hl=[a-z-]{2.5}','?__a=1',alpha)

    try:
        if check_url3 or check_url4 or check_url2 or check_url1:
            req = requests.get(final_url)
            get_status = requests.get(final_url).status_code
            get_content = req.content.decode('utf-8')

            if get_status == 200:
                print("\nDownloading the image...")
                find_pp = re.search(r'profile_pic_url_hd\":\"([^\'\'])',get_content)
                pp_link = find_pp.group()
                pp_final = re.sub('profile_pic_url_hd":"','',pp_link)
                file_size_request = requests.get(pp_final,steam=True)
                file_size = int(file_size_request.headers['Content-Length'])
