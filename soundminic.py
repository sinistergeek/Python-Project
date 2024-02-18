import random, sys, time

try:
    import playsound
except ImportError:
    print('The playsound module needs to be installed to run this program. On Windows, open a Command Prompt and run: pip install playsound On macOS and Linux, open a Terminal and run: pip3 install playsound')
    sys.exit()

print('''
Sound Mimic, by sinister geek Try to memorize a pattern of A S D F letters (each with its own sound) as it gets longer and longer.''')
input('Press Enter to begin...')
pattern=''
while True:
    print('\n'* 60)
    pattern = pattern + random.choice('ASDF')
    print('Pattern: ',end='')
    for letter in pattern:
        print(letter, end=' ',flush=True)
        playsound.playsound('sound' + letter + '.wav')
    time.sleep(1)
    print('\n' * 60)
    response = input('> ').upper()
    if response != pattern:
        print('Incorrect!')
        print('The pattern was',pattern)
    else:
        print('Correct!')
    for letter in pattern:
        playsound.playsound('sound' + letter + '.wav')

    if response != pattern:
        print('You socored',len(pattern) - 1, 'points.')
        print('Thanks for playing!')
        break

    time.sleep(1)
