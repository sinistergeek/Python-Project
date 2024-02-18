import random

try:
    import pyperclip

except ImportError:
    pass

def main():
    print('''
    sPoNgEcAsE, by sinister geek Enter the message
    ''')
    spongetext = englishToSpongecase(input('> '))
    print()
    print(spongetext)
    try:
         pyperclip.copy(spongetext)
         print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass

def englishToSpongecase(message):
    spongetext=''
