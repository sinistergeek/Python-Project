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
    print('The %sed message is:' % (myMode))
    print(translated)
    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.'%(myMode))
    except:
        pass

def checkKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print('There is an error in the key or symbol set.')
        return False
    return True

def encryptMessage(message,key):
    return translateMessage(message,key,'encrypt')

def decryptMessage(message,key):
    return translateMessage(message,key,'decrypt')
def translateMessage(message,key,mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        charsA,charsB = charsB,charsA

    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated


