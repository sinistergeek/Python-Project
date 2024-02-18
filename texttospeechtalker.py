import sys

try:
    import pyttsx3
except ImportError:
    print('Install pyttx3')
    sys.exit()
tts = pyttx3.init()
print('Text to Speech Talker')
print()
print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('> ')
    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    tts.say(text)
    tts.runAndWait()
