import random
try:
    import pyperclip
except ImportError:
    pass

def main():
    print('''
    L3375P34] <(leetspeek) 
    Enter  your leet message:
    ''')
    english = input('> ')
    print()
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)
    try:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')

