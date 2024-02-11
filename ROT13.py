try:
    import pyperclip
except ImportError:
    pass

UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('ROT13 Cipher')
print()

while True:
    print('Enter a message to encrypt/decrypt (or QUIT)')
    message = input('> ')
    if message.upper() == 'QUIT':
        break
    translated = ''
    for character in message:
        if character.isupper():
            transCharIndex = (UPPER_LETTERS.find(character) + 13)% 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            transCharIndex = (LOWER_LETTERS.find(character) + 13)%26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            translated += character

    print('This tanslated message is:')
    print(translated)
    print()
    try:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass
