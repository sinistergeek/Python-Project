try:
    import pyperclip
except ImportError:
    pass

VOWELS = ('a','e','i','o','u','y')

def main():
    print('''
    Igpay Atinlay(Pig Latin)
    Enter your message.''')
    pigLatin = englishToPigLatin(input('> '))
    print(pigLatin)
    try:
        pyperclip.copy(pigLatin)
        print('(Copied pig latin to clipboard)')
    except NameError:
        pass
