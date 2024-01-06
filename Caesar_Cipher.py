try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('Caesar Cipher, by sinister geek')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('Key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()


while True:
    print('Do you want to (e)ncrypt or (d)ecrypt')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break

    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').uppper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break


print('Enter the message to {}.'.format(mode))
message = message.upper()
translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)


    else:
        tanslated = translated + symbol
print(traslated)
