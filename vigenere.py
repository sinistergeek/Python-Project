try:
    import pyperclip

except ImportError:
    pass

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print(''' Vigenere Cipher''')
    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')
    while True:
        print('Please specify the key to use.')
        print('It can be word or any combination of letters:')
        response = input('> ').upper()
        if response.isalpha():
            myKey = response
            break
    print('Enter the message to {}'.format(myMode))
    myMyessage = input('> ')

    if myMode == 'encrypt':
        translated = encryptMessage(myMessage,myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage,myKey)
