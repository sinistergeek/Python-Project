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
    useUpper = False
    for character in message:
        if not character.isalpha():
            spongetext += character
            continue
        if useUpper:
            spongetext += character.upper()
        else:
            spongetext += character.lower()
        if random.randint(1,100) <= 90:
            useUpper = not useUpper
    return spongetext

if __name__ == '__main__':
    main()
