import re
import click
from proxytest import add_file_text_file
from proxytest import test_csv_file
from proxytest import test_single_proxy

def valid_proxy(ctx,param,value):
    validator = re.compile(r'(https|http|socks4|socks5):\/\/'
                           r'((?:[0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]{2,5})?'
                           r'|([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?)')

