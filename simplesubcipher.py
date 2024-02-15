import random
try:
    import pyperclip

except ImportError:
    pass
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
    print('''
    Simple Substitution Cipher, it has a one-to-one translation for each symbol in the plaintext and each symbol in the ciphertext.
    ''')
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
        if myMode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if checkKey(response):
                myKey = response
                break
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')
    if myMode = 'encrypt':
        translated = encryptMessage(myMessage,myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage,myKey)

