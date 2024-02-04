import random,time

deff slowSpacePrint(text,interval=0.1):
    for character in text:
        if character == 'I':
            print('i',end='',flush=True)
        else:
            print(character + '',end='',flush=True)
        time.sleep(interval)
    print()
    print()
