import sys, random,time
try:
    import bext
except ImportError:
    print('This program request the bext module, which you')
    print('can still by following the instruction at')
    print('https://pypi.org/project/Bext')
    sys.exit()


WIDTH,HEIGHT = bext.size()
