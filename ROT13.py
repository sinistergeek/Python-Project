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
