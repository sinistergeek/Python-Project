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


def englishToPigLatin(message):
    pigLatin = ''
    for word in message.split():
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin = pigLatin + prefixNonLetters + ' '
            continue
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters = word[-1] + suffixNonLetters
            word = word[:-1]

        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower()
        prefixConsonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]

        if prefixConsonants != '':
            word += prefixConsonants + 'ay'
        else:
            word += 'yay'

        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        pigLatin += prefixNonLetters + word + suffixNonLetters + ''
    return pigLatin
if __name__ == '__main__':
    main()

