import random,time

def slowSpacePrint(text,interval=0.1):
    for character in text:
        if character == 'I':
            print('i',end='',flush=True)
        else:
            print(character + '',end='',flush=True)
        time.sleep(interval)
    print()
    print()

slowSpacePrint('Magic fortune ball')
time.sleep(0.5)
slowSpacePrint('Ask me your yes/No QUESTION.')
input('> ')

replies = [
'Let Me think on this....',
'An interesting question...',
'Hmm. Are you sure you want to know....',
'Do you think some things are best left unknown....?',
'I might tell you, But you might not like the answer...',
'Yes...No...Maybe.. I wil think on it....',
'And what will you do when you know the answer? We shall see...',
'I shall consult my vision...',
'You may want to sit down for this...'
        ]
slowSpacePrint(random.choice(replies))
slowSpacePrint('I have an aswer...',0.2)
time.sleep(1)
answers = [
'Yes, for sure',
'My Answer is no',
'Ask me later',
'I am programmed to say yes',
'The stars say yes, But I say no',
'I Dunno maybe',
'Focus and ask, But i say no',
'Doubful, very doubtful',
'Affirmative',
'Yes, Though you may not like it',
'No, But you may wish it was so'
        ]
slowSpacePrint(random.choice(answers),0.5)
