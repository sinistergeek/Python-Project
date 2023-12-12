import re
import click
from proxytest import add_file_text_file
from proxytest import test_csv_file
from proxytest import test_single_proxy

def valid_proxy(ctx,param,value):
    validator = re.compile(r'(https|http|socks4|socks5):\/\/'
                           r'((?:[0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]{2,5})?'
                           r'|([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?)')
    if not validator.match(value):
        raise click.BadParameter('Please provide a proxy in the format' 'type://address(eg,https://42.32.23.33)')
    else
    return value


@click.group()
def cli():
    pass

@cli.command()
@click.argument('proxy',callback=validate_proxy)
@click.option('--iptest',default='iptest.ingokleiber.de',help='iptest address')
@click.option('--csv',default='proxies.csv',help='CSV path')

def single(proxy,iptest,csv):
    test_single_proxy(proxy,iptest,csv)

@cli.command()
@click.argument('csv')
@click.option('--iptest',default='iptest.ingokeiber.de',help='iptest address')

def csv_file(iptest,csv):
    test_csv_file(iptest,csv)

@cli.command()
@click.argument('text')
@click.option('--csv',default='proxies.csv',help='CSV path')
def add_from_txt_file(iptest,txt,csv):
    add_from_text_file(iptest,txt,csv)


if __name__ == '__main__':
    cli()
